#ifndef F_CPU
#define F_CPU 16000000UL // 16 MHz clock speed
#endif

#define UART_BAUD_RATE 1000000


#include <avr/io.h>
#include <util/delay.h>
#include <avr/interrupt.h>
#include <stdlib.h>
#include <stdbool.h>
#include "AX18ServoDriver.h"

#include "IOPorts_ATMega.h"
#include "uart.h"

void setID(unsigned char IDnumber);
void doServo(int Position);
void setBD(void);
void ledState(unsigned char Status);

#define THISID 0x55

int main(void)
{
	uart_init(UART_BAUD_SELECT(UART_BAUD_RATE,F_CPU));
	uart1_init(UART_BAUD_SELECT(UART_BAUD_RATE,F_CPU));
	DDRB = 0xFF;

	sei();

	//setBD();

	//doServo(50);

	unsigned long Position = 50;
	unsigned char	Position_L = Position & 0xFF;
	unsigned char	Position_H = (Position >> 8) & 0xFF;           // 16 bits - 2 x 8 bits variables
unsigned char buffer[2];
buffer[0] = Position_L;
buffer[1] = Position_H;
	AX18FWrite(BROADCAST_ID, AX_GOAL_POSITION_L, buffer, 2);

	while(1) //infinite loop
	{
// 		PORTB = PIN0_bm;
// 		_delay_ms(1000); 
// 		PORTB = 0x00; 
// 		ledState(1);
// 		doServo(0x00);		
// 		_delay_ms(1000);
// 		uart_puts("hoi sanda");
// 		ledState(0);
// 		doServo(0x3FF);
	}
}

void doServo(int Position) {

	char Position_H,Position_L;
	Position_L = Position & 0xFF;
	Position_H = (Position >> 8) & 0xFF;           // 16 bits - 2 x 8 bits variables

	unsigned char Checksum = ~(BROADCAST_ID + AX_GOAL_LENGTH + AX_WRITE_DATA + AX_GOAL_POSITION_L + Position_L + Position_H);	

	uart1_putc(AX_START);
	uart1_putc(AX_START);
	uart1_putc(BROADCAST_ID);
	uart1_putc(AX_GOAL_LENGTH);
	uart1_putc(AX_WRITE_DATA);
	uart1_putc(AX_GOAL_POSITION_L);
	uart1_putc(Position_L);
	uart1_putc(Position_H);
	uart1_putc(Checksum);
}

void setBD (void)
{
	long Baud = 1000000;
	unsigned char Baud_Rate = (2000000/Baud) - 1;
	//      unsigned char Baud_Rate = (Baud);
	unsigned char Checksum = ~(BROADCAST_ID + AX_BD_LENGTH + AX_WRITE_DATA + AX_BAUD_RATE + Baud_Rate);
	
	uart1_putc(AX_START);                 // Send Instructions over Serial
	uart1_putc(AX_START);
	uart1_putc(BROADCAST_ID);
	uart1_putc(AX_BD_LENGTH);
	uart1_putc(AX_WRITE_DATA);
	uart1_putc(AX_BAUD_RATE);
	uart1_putc(Baud_Rate);
	uart1_putc(Checksum);
}

void ledState (unsigned char Status)
{
	unsigned char Checksum = ~(THISID + AX_LED_LENGTH + AX_WRITE_DATA + AX_LED + Status);
	uart1_putc(AX_START);              // Send Instructions over Serial
	uart1_putc(AX_START);
	uart1_putc(THISID);
	uart1_putc(AX_LED_LENGTH);
	uart1_putc(AX_WRITE_DATA);
	uart1_putc(AX_LED);
	uart1_putc(Status);
	uart1_putc(Checksum);
}

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