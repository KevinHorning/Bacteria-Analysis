% Creates a variable for the image folder
myDir = 'training_data';

% Checks that given image folder exists. Gives error message if not found.
if ~isfolder(myDir)
  errorMsg = sprintf('Error: Directory not found:\n%s', myDir);
  uiwait(warndlg(errorMsg));
  return;
end

% Gets list of all files with the corresponding file extension
f = fullfile(myDir, '*.jpg');
theFiles = dir(f);
vector_img = zeros(28^2, length(theFiles ));

for k = 1 : length(theFiles)
  baseFile = theFiles(k).name;
  completeFile = fullfile(myDir, baseFile);
  disp(k)
  fprintf(1, 'Now reading %s\n', completeFile); %prints the current image being processed.
  img = imread(completeFile); %reads image
  img_resize = imresize(img, [28 28]); %resizes image
  img_gray = rgb2gray(img_resize); %turns image to grayscale
  vector_img(:,k) = img_gray(:); %vectorizes the image, places in matrix
end

csvwrite('traingingData.csv', vector_img'); %writes the vectorized images to csv file