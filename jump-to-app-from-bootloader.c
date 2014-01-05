// From zyp, also available in his suzumbiachiasdfasdf repostiroy I believe

void chainload(uint32_t offset) {
        SCB.VTOR = offset;

        asm volatile("ldr sp, [%0]; ldr %0, [%0, #4]; bx %0" :: "r" (offset));
}
