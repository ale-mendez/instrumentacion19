//// ****** THIS FILE IS AUTOGENERATED ******
////
////          >>>> DO NOT CHANGE <<<<
////
/// 
///  Filename; C:\Users\LBT\Dropbox\Instrumentacion y control\ProyectoFinal\lantz\run.py
///  Source class: LEDDriver
///  Generation timestamp: 2019-06-25T18:10:47.799727
///  Class code hash: 8647375a3d456c77a25af7a8712a5951c71a1594
///
/////////////////////////////////////////////////////////////

#ifndef inodriver_bridge_h
#define inodriver_bridge_h

#include <Arduino.h>

#include "SerialCommand.h"

#include "inodriver_user.h"

const char COMPILE_DATE_TIME[] = __DATE__ " " __TIME__;

void ok();
void error(const char*);
void error_i(int);
void bridge_loop();
void bridge_setup();

void getInfo();
void unrecognized(const char *);
void wrapperGet_LED(); 
void wrapperSet_LED(); 


#endif // inodriver_bridge_h