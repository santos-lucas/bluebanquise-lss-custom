add the following line to "/etc/pam.d/password-auth" ??


session     required      pam_exec.so type=open_session /etc/security/limits.sh
