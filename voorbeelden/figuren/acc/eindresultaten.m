sample = ['Accelerometer','Luchtdruk','Slinger']
sample_val = [1, 2, 3];
hoogte = [8.31,8.70,8.0];
onzekerheid = [0.5,1.0,1.5];

% labels & legend zelf aanpassen in createFit

%plot(sample,hoogte, '*');
errorbar(sample_val(1), hoogte(1), onzekerheid(1), 'vertical', '>', 'Color', 'r');
hold on
errorbar(sample_val(2), hoogte(2), onzekerheid(2), 'vertical', '^', 'Color', 'r');
hold on
errorbar(sample_val(3), hoogte(3), onzekerheid(3), 'vertical', 'v', 'Color', 'r');
hold on

legend('Accelerometer', 'Luchtdruk', 'Slinger', 'Location' ,'SouthWest')


xlim([0 4])
ylim([6 10])

% Correcte significantie maken voor plot 1
xtickformat('%.1f')
ytickformat('%.1f')

% Punt naar comma veranderen voor de de assen van plot 1
x = get(gca, 'XTickLabel');
nieuw_x = strrep(x(:),'.',',');
set(gca, 'XTickLabel', nieuw_x)
y = get(gca, 'YTickLabel');
nieuw_y = strrep(y(:),'.',',');
set(gca, 'YTickLabel', nieuw_y)

% Legend
%figure( 'Name', 'untitled fit 1', 'Location', 'NorthEast');

% Label axes
ylabel('Hoogte $h$ [m]', 'Interpreter', 'latex')
xlabel('Meting soort [-]', 'Interpreter', 'latex')
grid on


