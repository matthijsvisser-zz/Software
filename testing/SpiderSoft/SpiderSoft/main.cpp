/*
 * SpiderSoft.cpp
 *
 * Created: 1/12/2016 1:40:49 PM
 * Author : Sander van Doesburg
 */ 

#ifndef F_CPU
#define F_CPU 16000000UL // 16 MHz clock speed
#endif

#define UART_BAUD_RATE 1000000
#define UART_BAUD_RATE_XBEE 115200

#include <avr/io.h>
#include <util/delay.h>
#include <avr/interrupt.h>
#include <stdlib.h>
#include <stdio.h>

#include "AX18ServoDriver.h"
#include "IOPorts_ATMega.h"
#include "uart.h"
#include "timer.h"
#include "XbeeCom.h"

int main(void)
{
	uart_init(UART_BAUD_SELECT(UART_BAUD_RATE_XBEE,F_CPU));
	uart1_init(UART_BAUD_SELECT(UART_BAUD_RATE,F_CPU));
	
    /* Replace with your application code */
    while (1) 
    {
    }
}

