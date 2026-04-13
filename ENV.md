
git submodule update --init --recursive


git submodule sync
git submodule update --init --recursive --force


float vectored_hover_gain = 2;
float des_pitch_cd = quadplane.attitude_control->get_att_target_euler_cd().y;
int32_t pitch_error_cd = (des_pitch_cd - quadplane.ahrs_view->pitch_sensor) * 0.5;
float extra_pitch = constrain_float(pitch_error_cd, -SERVO_MAX, SERVO_MAX) / SERVO_MAX;
float extra_sign = extra_pitch > 0?1:-1;
float extra_elevator = 0;
if (!is_zero(extra_pitch) && quadplane.in_vtol_mode()) {
    extra_elevator = extra_sign * powf(fabsf(extra_pitch), vectored_hover_power) * SERVO_MAX;
}
tilt_motor  = extra_elevator + tilt_motor * vectored_hover_gain;
SRV_Channels::set_output_scaled(SRV_Channel::k_motor_tilt, tilt_motor);
