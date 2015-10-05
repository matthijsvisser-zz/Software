/*
 * timer.h
 *
 * Created: 10/1/2015 12:08:52 PM
 *  Author: Sander van Doesburg
 */ 


#ifndef TIMER_H_
#define TIMER_H_

#include <util/atomic.h>

#define MAX_TIMER_VALUE 65536
#define MILLI_TO_TICKS(millis) (F_CPU/1024000)*millis

unsigned long timerOverflows;
unsigned long diffTimeCnt0;
unsigned long diffOFCount0;
unsigned long diffTimeCnt1;
unsigned long diffOFCount1;
unsigned long diffTimeCnt2;
unsigned long diffOFCount2;

void startTickTimer(void);
unsigned long diffTimer0(void);
unsigned long diffTimer1(void);
unsigned long diffTimer2(void);
unsigned long getTick(void);
void stopTickTimer(void);



#endif /* TIMER_H_ */