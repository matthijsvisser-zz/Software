/*
 * SetServoID.h
 *
 * Created: 11-9-2015 12:28:19
 *  Author: mv
 */ 
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
void ledState(unsigned char Status);