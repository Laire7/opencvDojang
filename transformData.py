import cv2, os
import numpy as np
import shutil

class Transform:
    def __init__(self, imgPath):
        self.imgPath = imgPath
        self.img = cv2.imread(imgPath)
        # Check if image loaded
        if self.img is None:
            print("Error: Could not load image.")
            exit()
    
    def changeColor(self, mask_range_lower, mask_range_upper, hmin, hmax):
        #Resize img    
        img = cv2.resize(self.img, (2000,2000))

        # Convert the image to HSV color space
        hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

        # Create a mask for yellow color
        color_mask = cv2.inRange(hsv_img, mask_range_lower, mask_range_upper)

        ## Create a window and trackbars for adjusting the hue of the yellow areas
        # cv2.namedWindow('Color Adjuster')

        # while True:
        # Create an HSV version of the yellow mask with the new hue, saturation, and value
        modified_hsv = hsv_img.copy()
        modified_hsv[color_mask > 0, 0] = np.random.randint(hmin, hmax+1, size=np.count_nonzero(color_mask))  # Apply random hues between 120 and 160

        # Convert back to BGR to display
        modified_img = cv2.cvtColor(modified_hsv, cv2.COLOR_HSV2BGR)

        # Combine the original image with the modified parts
        final_img = cv2.bitwise_and(modified_img, modified_img, mask=color_mask)  # Apply color change to yellow parts
        final_img = cv2.add(final_img, cv2.bitwise_and(img, img, mask=cv2.bitwise_not(color_mask)))  # Keep other parts intact
        return final_img

        #     # Display the original and the result side by side
        #     cv2.imshow('Color Adjuster', final_img)

        #     # Break the loop if 'q' is pressed
        #     if cv2.waitKey(1) & 0xFF == ord('q'):
        #         break

        # cv2.destroyAllWindows()
    
class DataAug:
        def __init__(self, imgFileDir):
            self.imgFileDir = imgFileDir
            self.imgListDir = os.listdir(imgFileDir)
            self.imgList = self.getImgList(imgFileDir)
                
        def getImgList(self,imgListDir):
            imgList = []
            for imgName in self.imgListDir:
                imgPath = self.imgFileDir + '/' + str(imgName)
                img = Transform(imgPath)
                imgList.append(img)
            
            return imgList
                        
        def colorSettings(self, low_mask_range, high_mask_range, hmin, hmax):
            self.low_mask_range = low_mask_range
            self.high_mask_range = high_mask_range
            self.hmin = hmin
            self.hmax = hmax
            
        def dataAug(self, transform, folderName=None):
            if folderName == None:
                folderName = transform
            transformImgList = []
            if transform == "camaflouge":
                for img in self.imgList:
                    transformImgList.append(img.changeColor(self.low_mask_range, self.high_mask_range, self.hmin, self.hmax))
            self.createData(transformImgList, folderName)
            return transformImgList
        
        def createData(self, dataList, folderName):
            # Create Folder
            folderPath = os.path.join(os.getcwd(), self.imgFileDir.split('/')[0], folderName, self.imgFileDir.split('/')[2])
            print(f'folderPath: {folderPath}')
            if os.path.exists(folderPath):
                shutil.rmtree(folderPath)    
            os.makedirs(folderPath)
            
            # Create Files
            for i, data in enumerate(dataList):
                fileName = str(folderName + '_' + self.imgListDir[i])
                filePath = os.path.join(folderPath, fileName)
                img = cv2.imwrite(filePath, dataList[i])
                img_show = cv2.imread(filePath)
                cv2.imshow('img', img_show)
                cv2.waitKey()
                cv2.destroyAllWindows()
                    
if __name__ == "__main__":
    # banana_imgPath = 'snack/orig/banana/10095_0_s_2.jpg'
    banana_mask_range_lower = np.array([20, 100, 100])
    banana_mask_range_upper = np.array([30, 255, 255])
    banana_hmin = 120
    banana_hmax = 160

    # bananaPurple = Transform(banana_imgPath)
    # bananaAug.changeColor(banana_mask_range_lower, banana_mask_range_upper, banana_hmin, banana_hmax)
    
    # blueberry_imgPath = 'snack/orig/blueberry/10060_0_s_2.jpg'
    blueberry_mask_range_lower = np.array([110, 0, 0])
    blueberry_mask_range_upper = np.array([195, 255, 255])
    blueberry_hmin = 200
    blueberry_hmax = 210
    
    # blueberryYellow = Transform(blueberry_imgPath)
    # bananaAug.changeColor(blueberry_mask_range_lower, blueberry_mask_range_upper, blueberry_hmin, blueberry_hmax)
    
    camaflougeDict = {'banana': [banana_mask_range_lower, banana_mask_range_upper, banana_hmin, banana_hmax],
                      'blueberry': [blueberry_mask_range_lower, blueberry_mask_range_upper, blueberry_hmin, blueberry_hmax]}
    
    dataDir = 'snack/orig'
    dataList = os.listdir(dataDir) 
    sampleList = []
    for i in range(0,2):
        sampleList.append(dataList[i])
    
    for snackFolder in sampleList:
        snackFolderPath = os.path.join(dataDir, snackFolder)
        snackAug = DataAug(snackFolderPath)
        snackAug.colorSettings(camaflougeDict[snackFolder][i] for i in range(len(camaflougeDict[snackFolder])))
        snackAug.dataAug("camaflouge")
        
    # banana_dataPath = 'snack/orig/banana'
    # bananaAug = DataAug(banana_dataPath)
    # bananaAug.colorSettings(banana_mask_range_lower, banana_mask_range_upper, banana_hmin, banana_hmax)
    # bananaAug.dataAug("camaflouge")
    
    # blueberry_dataPath = 'snack/orig/blueberry'
    # blueberryAug = DataAug(blueberry_dataPath)
    # blueberryAug.colorSettings(blueberry_mask_range_lower, blueberry_mask_range_upper, blueberry_hmin, blueberry_hmax)
    # blueberryAug.dataAug("camaflouge")