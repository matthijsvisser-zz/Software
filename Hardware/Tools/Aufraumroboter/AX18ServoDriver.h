       // EEPROM AREA  ///////////////////////////////////////////////////////////
#define AX_MODEL_NUMBER_L           0x00
#define AX_MODEL_NUMBER_H           0x01
#define AX_VERSION					0x02
#define AX_ID						0x03
#define AX_BAUD_RATE			    0x04
#define AX_RETURN_DELAY_TIME        0x05
#define AX_CW_ANGLE_LIMIT_L         0x06
#define AX_CW_ANGLE_LIMIT_H         0x07
#define AX_CCW_ANGLE_LIMIT_L        0x08
#define AX_CCW_ANGLE_LIMIT_H        0x09
//#define AX_SYSTEM_DATA2			 10
#define AX_LIMIT_TEMPERATURE        0x0B
#define AX_DOWN_LIMIT_VOLTAGE       0x0C
#define AX_UP_LIMIT_VOLTAGE         0x0D
#define AX_MAX_TORQUE_L			 	0x0E
#define AX_MAX_TORQUE_H			 	0x0F
#define AX_RETURN_LEVEL			 	0x10
#define AX_ALARM_LED			    0x11
#define AX_ALARM_SHUTDOWN           0x12
//#define AX_OPERATING_MODE           19
//#define AX_DOWN_CALIBRATION_L       20
//#define AX_DOWN_CALIBRATION_H       21
//#define AX_UP_CALIBRATION_L         22
//#define AX_UP_CALIBRATION_H         23

        // RAM AREA  //////////////////////////////////////////////////////////////
#define AX_TORQUE_ENABLE			0x18
#define AX_LED						0x19
#define AX_CW_COMPLIANCE_MARGIN		0x1A
#define AX_CCW_COMPLIANCE_MARGIN	0x1B
#define AX_CW_COMPLIANCE_SLOPE		0x1C
//#define AX_CCW_COMPLIANCE_SLOPE     29
#define AX_GOAL_POSITION_L			0x1E
#define AX_GOAL_POSITION_H			0x1F
#define AX_GOAL_SPEED_L				0x20
#define AX_GOAL_SPEED_H				0x21
#define AX_TORQUE_LIMIT_L			0x22
#define AX_TORQUE_LIMIT_H			0x23
#define AX_PRESENT_POSITION_L		0x24
#define AX_PRESENT_POSITION_H		0x25
#define AX_PRESENT_SPEED_L			0x26
#define AX_PRESENT_SPEED_H			0x27
#define AX_PRESENT_LOAD_L			0x28
#define AX_PRESENT_LOAD_H			0x29
#define AX_PRESENT_VOLTAGE			0x2A
#define AX_PRESENT_TEMPERATURE		0x2B
#define AX_REGISTERED_INSTRUCTION	0x2C
//#define AX_PAUSE_TIME			   45
#define AX_MOVING					0x2E
#define AX_LOCK						0x2F
#define AX_PUNCH_L					0x30
#define AX_PUNCH_H					0x31

    // Status Return Levels ///////////////////////////////////////////////////////////////
#define AX_RETURN_NONE				0x00
#define AX_RETURN_READ				0x01
#define AX_RETURN_ALL				0x02

    // Instruction Set ///////////////////////////////////////////////////////////////
#define AX_PING						0x01
#define AX_READ_DATA				0x02
#define AX_WRITE_DATA				0x03
#define AX_REG_WRITE				0x04
#define AX_ACTION					0x05
#define AX_RESET					0x06
#define AX_SYNC_WRITE				0x83

        // Specials ///////////////////////////////////////////////////////////////
#define _OFF						0x00
#define _ON							0x01
#define LEFT						0x00
#define RIGHT						0x01
#define AX_BYTE_READ			    0x01
#define AX_BYTE_READ_POS			0x02
#define AX_RESET_LENGTH				0x02
#define AX_ACTION_LENGTH			0x02
#define AX_ID_LENGTH				0x04
#define AX_BD_LENGTH				0x04
#define AX_TEM_LENGTH				0x04
#define AX_VOLT_LENGTH				0x04
#define AX_LED_LENGTH				0x04
#define AX_TORQUE_LENGTH			0x05
#define AX_TORQUE_MAX_LENGTH		0x05
#define AX_ALARM_LENGTH				0x04
#define AX_POS_LENGTH				0x04
#define AX_LOAD_LENGTH				0x04
#define AX_RETURN_LENGTH			0x04
#define AX_SPEED_LENGTH				0x05
#define AX_GOAL_LENGTH				0x05
#define AX_READ_SPEED_LENGTH		0x04
#define AX_GOAL_SP_LENGTH			0x07
#define AX_ACTION_CHECKSUM			0xFA
#define BROADCAST_ID				0xFE
#define AX_START					0xFF
#define AX_CCW_AL_L					0XFF 
#define AX_CCW_AL_H					0x03
#define BUFFER_SIZE					64
#define TIME_OUT					10
#define READ_TIME_OUT				2
#define TX_DELAY_TIME				12			          // 12  delay is relerative to Baudrate, slow speed more delay is needed
#define TX_BD_DELAY_TIME			500
#define TX_READ_DELAY_TIME			12			          // 12 delay is relerative to Baudrate, slow speed more delay is needed

void AX18FWrite(unsigned char id, unsigned char address, unsigned char *data, unsigned char length);
void AX18Position(unsigned char id, unsigned long pos);
void AX18Speed(unsigned char id, unsigned long speed);
unsigned char unsigned16ToUnsigned8Lower(unsigned long data);
unsigned char unsigned16ToUnsigned8Higher(unsigned long data);
