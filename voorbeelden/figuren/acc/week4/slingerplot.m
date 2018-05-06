sample = importdata('slinger_modified_1.csv'); % column 2 3 4 zijn xyz acc
sample = sample.data;

time = sample(:,2);
time = time - time(1,1);
index = sample(:,16);
acc_x = sample(:,3);
acc_y = sample(:,4); 
acc_z = sample(:,5);


min_val = 17000;
max_val = 19500;
time = time(min_val:max_val);
index = index(min_val:max_val);
acc_x = acc_x(min_val:max_val);
acc_y = acc_y(min_val:max_val);
acc_z = acc_z(min_val:max_val);

plot(index,acc_x, '.')
xlabel('t (milliseconds)')
ylabel('X(t)')

% FFT

Fs = 6.25;            % Sampling frequency                    
T = 1/Fs;             % Sampling period       
L = 1500;             % Length of signal
t = (0:L-1)*T;        % Time vector

Y = fft(acc_x);

P2 = abs(Y/L);
P1 = P2(1:L/2+1);
P1(2:end-1) = 2*P1(2:end-1);

f = Fs*(0:(L/2))/L;
plot(f,P1) 
xlabel('f (Hz)')
ylabel('Amplitude [-]')


%plot(time, y)


%ylim([0 0.006])% stel limieten in om in te zoomen op frequenties
%xlim([0 0.3])
grid on

%xlabel('Frequentie (Hz)')
%ylabel('Amplitude [-]')