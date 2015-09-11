void setID (unsigned char IDnumber)
{
	unsigned char checksum = ~(BROADCAST_ID + AX_LED_LENGTH + AX_WRITE_DATA + AX_ID + IDnumber);
	uart1_putc(AX_START);
	uart1_putc(AX_START);
	uart1_putc(BROADCAST_ID);
	uart1_putc(AX_LED_LENGTH);
	uart1_putc(AX_WRITE_DATA);
	uart1_putc(AX_ID);
	uart1_putc(IDnumber);
	uart1_putc(checksum);
}