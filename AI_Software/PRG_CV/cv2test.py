import cv2 as cv
import sys

#화소의 위치는 Y X 순서로 표현한다.

def main():
    print(cv.__version__, "\n\n")

    img = cv.imread("soccer.jpg")

    if(img is None):
        sys.exit("이미지를 불러올 수 없습니다.")
        return
    
    print("영상 데이터 shape:", img.shape)

    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    gray_half = cv.resize(gray, (0, 0), fx=0.5, fy=0.5)

    # 글자 넣기
    # 이미지, 문자열, 시작 위치, 글꼴, 크기, 색상, 두께
    cv.putText(img, "2036.03.20", (60, 100), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    cv.putText(gray, "2036.03.20", (60, 100), cv.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
    cv.putText(gray_half, "2036.03.20", (60, 100), cv.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

    cv.imshow("soccer", img)
    cv.imshow("soccer gray", gray)
    cv.imshow("soccer gray half", gray_half)

    cv.waitKey(0)
    cv.destroyAllWindows()


main()