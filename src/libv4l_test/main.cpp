#define Esc 27
#include <opencv2/opencv.hpp>
#include <iostream>
#include <stdio.h>
#include "v4ldevice.h"

int main(int argc, char** args) {
    //<<??n
    int width=640, height=400;
    open_device("/dev/video0");
    init_device(width, height, 300);

    //-?x??n?
    start_capturing();

    //?????hMat???n
    unsigned char* ImageBuffer = NULL;
    cv::Mat src(height, width, CV_8UC1);
    cv::Mat dst; 

    cv::namedWindow("image", cv::WINDOW_AUTOSIZE);
    while (true) {

        //-?x??
        ImageBuffer = snapFrame();
        if (ImageBuffer != NULL) {
            memcpy(src.data, ImageBuffer, src.step * src.rows); //?????Mat???kxQ!Y
            cvtColor(src, dst, cv::COLOR_BayerGB2RGB); //SSLBayer	?
        } else {
            std::cerr << "no image buffer retrieved!" << std::endl;
        }
        cv::imshow("image", dst);
        if (cv::waitKey(1) == Esc) {
            cv::destroyAllWindows();
            break;
        }
    }

}

