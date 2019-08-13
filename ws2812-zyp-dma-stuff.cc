Source: https://cgit.jvnv.net/arcin/tree/arcin/main.cpp?id=1cb55ca#n64

class WS2812B {
	private:
		uint8_t dmabuf[25];
		volatile uint32_t cnt;
		volatile bool busy;
		
		void schedule_dma() {
			cnt--;
			
			DMA1.reg.C[6].NDTR = 25;
			DMA1.reg.C[6].MAR = (uint32_t)&dmabuf;
			DMA1.reg.C[6].PAR = (uint32_t)&TIM4.CCR3;
			DMA1.reg.C[6].CR = (0 << 10) | (1 << 8) | (1 << 7) | (0 << 6) | (1 << 4) | (1 << 1) | (1 << 0);
		}
		
		void set_color(uint8_t r, uint8_t g, uint8_t b) {
			uint32_t n = 0;
			
			for(uint32_t i = 8; i-- > 0; n++) {
				dmabuf[n] = g & (1 << i) ? 58 : 29;
			}
			
			for(uint32_t i = 8; i-- > 0; n++) {
				dmabuf[n] = r & (1 << i) ? 58 : 29;
			}
			
			for(uint32_t i = 8; i-- > 0; n++) {
				dmabuf[n] = b & (1 << i) ? 58 : 29;
			}
			
			dmabuf[n] = 0;
		}
		
	public:
		void init() {
			RCC.enable(RCC.TIM4);
			RCC.enable(RCC.DMA1);
			
			Interrupt::enable(Interrupt::DMA1_Channel7);
			
			TIM4.ARR = (72000000 / 800000) - 1; // period = 90, 0 = 29, 1 = 58
			TIM4.CCR3 = 0;
			
			TIM4.CCMR2 = (6 << 4) | (1 << 3);
			TIM4.CCER = 1 << 8;
			TIM4.DIER = 1 << 8;
			
			GPIOB[8].set_af(2);
			GPIOB[8].set_mode(Pin::AF);
			GPIOB[8].set_pull(Pin::PullNone);
			
			TIM4.CR1 = 1 << 0;
			
			Time::sleep(1);
			
			update(0, 0, 0);
		}
		
		void update(uint8_t r, uint8_t g, uint8_t b) {
			set_color(r, g, b);
			
			cnt = 15;
			busy = true;
			
			schedule_dma();
		}
		
		void irq() {
			DMA1.reg.C[6].CR = 0;
			DMA1.reg.IFCR = 1 << 24;
			
			if(cnt) {
				schedule_dma();
			} else {
				busy = false;
			}
		}
};

WS2812B ws2812b;

template <>
void interrupt<Interrupt::DMA1_Channel7>() {
	ws2812b.irq();
}
