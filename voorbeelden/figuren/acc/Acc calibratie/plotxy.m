sample = importdata('call_6.csv'); % column 2 3 4 zijn xyz acc

time = sample(:,1);
time = time - time(1,1); % start waarde van de tijd afhalen
time = time/(60^2); % omzetten naar uren
time = time/24; % omzetten naar dagen

acc_x = sample(:,2);
acc_y = sample(:,3); 
acc_z = sample(:,4);
humidity = sample(:,5);
temp_from_hum = sample(:,6);
temp_from_pressure = sample(:,7);
pressure = sample(:,8);
compass_x = sample(:,9);
compass_y = sample(:,10);
compass_z = sample(:,11);
gyro_x = sample(:,12);
gyro_y = sample(:,13);
gyro_z = sample(:,14);

z = sin(acc_x)+cos(acc_y);

plot(time, acc_z, '.')

xlabel('Tijd [dagen]', 'Interpreter', 'latex')
ylabel('Versnelling in $g$ [m/s$^2$]', 'Interpreter', 'latex')
grid on

