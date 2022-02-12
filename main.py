import cv2 as cv


def main():
    img = cv.imread('a.png')
    font = cv.FONT_HERSHEY_SCRIPT_SIMPLEX
    cv.putText(img, "Neerd", (120, 490), font, 4, (0, 0, 0), 2)

    cv.imwrite("tree.png", img)
    cv.imshow("tree", img)

    cv.waitKey(0)
    cv.destroyAllWindows()


if __name__ == '__main__':
    main()