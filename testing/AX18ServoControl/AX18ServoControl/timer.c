/*
 * timer.c
 *
 * Created: 10/1/2015 12:09:06 PM
 *  Author: Sander van Doesburg
 */ 
#include "timer.h"


void startTickTimer(void) {
	
	// Reset timer overflow counter
	timerOverflows = 0;
	diffTimeCnt0 = 0;
	diffOFCount0 = 0;
	diffTimeCnt1 = 0;
	diffOFCount1 = 0;
	diffTimeCnt2 = 0;
	diffOFCount2 = 0;
	
	// Config timer 1 as normal mode
	TCCR1A = 0;
	
	// Set timer source as sysCLK / 1024
	TCCR1B |= (1 << CS12) | (1 << CS10);
	
	// Enable overflow interrupt
	TIMSK1 |= (1 << TOIE1);
	
	// Reset timer
	TCNT1 = 0;
	
	sei();
	
}

// returns differential ticks since last call
unsigned long diffTimer0(void) {
	unsigned long Dtime = 0;
	
	// Check if we had an overflow
	if(diffTimeCnt0 > getTick()) {
		Dtime = (MAX_TIMER_VALUE - diffTimeCnt0) + getTick();
		} else {
		Dtime = getTick() - diffTimeCnt0;
	}
	
	
	diffTimeCnt0 = getTick();
	diffOFCount0 = timerOverflows;
	
	return Dtime;
}

// returns differential ticks since last call
unsigned long diffTimer1(void) {
	unsigned long Dtime = 0;
	
	// Check if we had an overflow
	if(diffTimeCnt1 > getTick()) {
		Dtime = (MAX_TIMER_VALUE - diffTimeCnt1) + getTick();
		} else {
		Dtime = getTick() - diffTimeCnt1;
	}
	
	
	diffTimeCnt1 = getTick();
	diffOFCount1 = timerOverflows;
	
	return Dtime;
}

// returns differential ticks since last call
unsigned long diffTimer2(void) {
	unsigned long Dtime = 0;
	
	// Check if we had an overflow
	if(diffTimeCnt2 > getTick()) {
		Dtime = (MAX_TIMER_VALUE - diffTimeCnt2) + getTick();
		} else {
		Dtime = getTick() - diffTimeCnt2;
	}
	
	
	diffTimeCnt2 = getTick();
	diffOFCount2 = timerOverflows;
	
	return Dtime;
}

// F_CPU / 1024
// 15,625kHz @ 16MHz
unsigned long getTick(void) {
	
	unsigned long cnt;
	 ATOMIC_BLOCK(ATOMIC_FORCEON)
	 {
		 cnt = TCNT1;
	 }
	 return cnt;
}

void stopTickTimer(void) {
	TCCR1B = 0;
}

ISR(TIMER1_OVF_vect) {
	timerOverflows++;
}