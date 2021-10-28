# FabricDefectDetection
A visual tool for defect detection of woven fabric

**Original Picture:** </br>
<img src="https://user-images.githubusercontent.com/70928881/139300363-df704542-616a-4008-8dd4-d4b601f61705.jpg" width="600"/>

**Median filter:** </br>
Median filtering can well preserve the edge information of the original image and will not affect subsequent operations. So first use median filtering to process the original image to filter out the noise, the effect is as follows: </br>
<img src="https://user-images.githubusercontent.com/70928881/139300581-a3cbb245-ef81-4757-98e7-34f937d30455.jpg" width="600"/>

**Use Canny edge detection algorithm to extract edge information:** </br>
Because the pattern of the flawless woven cloth is arranged in an orderly manner, there is no sudden change. Therefore, the use of edge detection means can effectively detect the location of the flaw. The Canny detection algorithm is currently the best detection algorithm. We use this method for edge detection. The effect is as follows: </br>
<img src="https://user-images.githubusercontent.com/70928881/139300719-c618bc6d-7ed2-4537-a272-dcd16aada450.jpg" width="600"/>

**Fill the inside of the contour through the closing operation:** </br>
Through edge detection, only the outline of the flaw is obtained. Therefore, the closed calculation algorithm is used to fill the defects inside, and the visual effect is better. The closed operation is a method of mathematical morphology, which expands first and then corrodes, which can fill the voids in the binary image. After testing, the effect is as follows: </br>
<img src="https://user-images.githubusercontent.com/70928881/139300866-77d749ee-d10b-401f-b8c6-4c90c4fbe547.jpg" width="600"/>

**UI:** </br>
We use Python's PyQt library to achieve visualization, detection prompts and visualization effects are shown in the following figure: </br>
![UI](https://user-images.githubusercontent.com/70928881/139301212-5db46ba3-5698-4935-a430-83df8b4996fc.jpg)
