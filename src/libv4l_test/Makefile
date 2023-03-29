all: opencv-test

opencv-test: main.cpp v4ldevice.cpp
	$(CXX) -Wall -g -O0 -o opencv-test main.cpp v4ldevice.cpp $(shell pkg-config --libs-only-l opencv libv4l2)
	# g++ -Wall -g -O0 -o opencv_test main.cpp v4ldevice.cpp $(pkg-config opencv libv4l2 --cflags --libs)

clean:
	$(RM) *.o
	$(RM) opencv-test

