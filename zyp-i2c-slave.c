// Source: https://paste.jvnv.net/view/9Hw48
#include <stdbool.h>
#include <stdint.h>

// Required functions.
void set_scl(bool value);
void set_sda(bool value);
bool get_scl();
bool get_sda();

// Callback types.
typedef bool (*addr_cb_t)(uint8_t addr);
typedef uint8_t (*read_cb_t)();
typedef void (*write_cb_t)(uint8_t data);

enum i2cs_state_t {
	I2CS_IDLE,
	I2CS_ADDR,
	I2CS_READ,
	I2CS_WRITE,
	I2CS_IGNORE
};

typedef enum i2cs_state_t i2cs_state_t;

struct i2cs_ctx_t {
	addr_cb_t addr_cb;
	read_cb_t read_cb;
	write_cb_t write_cb;
	
	i2cs_state_t state;
	uint8_t data;
	uint8_t data_cnt;
	bool ack;
};

typedef struct i2cs_ctx_t i2cs_ctx_t;

// Call to signal pin changed.
void sda_changed(i2cs_ctx_t* ctx) {
	if(get_scl()) {
		// Start/stop/repeat start condition, handle.
		
		if(get_sda()) {
			// Got stop condition.
			ctx->state = I2CS_IDLE;
			
		} else {
			// Got start condition.
			ctx->state = I2CS_ADDR;
			
			// Clear data.
			ctx->data = 0;
			ctx->data_cnt = 0;
		}
	} else {
		// Data transition, ignore.
	}
}

void scl_changed(i2cs_ctx_t* ctx) {
	if(ctx->state == I2CS_IDLE || ctx->state == I2CS_IGNORE) {
		return;
	}
	
	bool scl = get_scl();
	bool sda = get_sda();
	
	if(scl && ctx->ack) {
		return;
	}
	
	if(!scl && ctx->ack) {
		// ACK sent, de-assert SDA.
		set_sda(1);
		ctx->ack = false;
	}
	
	if(scl && (ctx->state == I2CS_ADDR || ctx->state == I2CS_WRITE)) {
		ctx->data = (ctx->data << 1) | sda;
		ctx->data_cnt++;
		
		return;
	}
	
	if(!scl && ctx->state == I2CS_ADDR && ctx->data_cnt == 8) {
		// Stretch clock.
		set_scl(0);
		
		// Call addr callback.
		if(ctx->addr_cb(ctx->data)) {
			// Clear data.
			ctx->data = 0;
			ctx->data_cnt = 0;
			
			// Send ACK.
			set_sda(0);
			ctx->ack = true;
			
			if(ctx->data & 1) {
				ctx->state = I2CS_READ;
			} else {
				ctx->state = I2CS_WRITE;
			}
		} else {
			ctx->state = I2CS_IGNORE;
		}
		
		// Stop stretching clock.
		set_scl(1);
		
		return;
	}
	
	if(!scl && ctx->state == I2CS_WRITE && ctx->data_cnt == 8) {
		// Stretch clock.
		set_scl(0);
		
		// Call write callback.
		ctx->write_cb(ctx->data);
		
		// Clear data.
		ctx->data = 0;
		ctx->data_cnt = 0;
		
		// Send ACK.
		set_sda(0);
		ctx->ack = true;
		
		// Stop stretching clock.
		set_scl(1);
		
		return;
	}

	if(!scl && ctx->state == I2CS_READ) {
		if(ctx->data_cnt == 0) {
			ctx->data = ctx->read_cb();
		}
	}
}
