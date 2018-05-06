N =5;

fileID = fopen('bigfile.txt');

formatSpec = '%s %f %f %f %s';

y = []

k = 0;
while ~feof(fileID)
	k = k+1;
	C = textscan(fileID,formatSpec,N,'CommentStyle','##','Delimiter','\t');
	y = y + c{2}
	scatter(C{2},C{3})
    
end