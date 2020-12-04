#include <stdio.h>
#include <iostream>
#include <time.h>
#include <conio.h>
#include <windows.h>

using namespace std;

enum eDir { STOP = 0, LEFT = 1, UPLEFT = 2, DOWNLEFT = 3, RIGHT = 4, UPRIGHT = 5, DOWNRIGHT = 6 };

class cBall
{
    private:
        int x, y;
        int originalx, originaly;
        eDir direction;

    public:
        cBall(int posx, int posy)
        {
            originalx = posx;
            originaly = posy;
            x = posx; y = posy;
            direction = STOP;
        }

        void Reset()
        {
            x = originalx; y = originaly;
            direction = STOP;
        }

        void changeDirection(eDir d)
        {
            direction = d;
        }
        void randomDirection()
        {
            direction = (eDir)((rand() % 6) + 1);
        }
        inline int getX() { return x; }
        inline int getY() { return y; }
        inline eDir getDir() { return direction; }

        void Move()
        {
            switch (direction)
            {
                case STOP:
                    break;
                case LEFT:
                    x--;
                    break;
                case RIGHT:
                    x++;
                    break;
                case UPLEFT:
                    x--; y--;
                    break;
                case DOWNLEFT:
                    x--; y++;
                    break;
                case UPRIGHT:
                    x++; y--;
                    break;
                case DOWNRIGHT:
                    x++; y++;
                    break;
                default:
                    break;
            }
        }
        friend ostream & operator << (ostream & o, cBall c)
        {
            o << "Ball [" << c.x << "," << c.y << "][" << c.direction << "]";
            return o;
        }
};

class cPaddle
{
    private:
        int x, y;
        int originalx, originaly;
    public:
        cPaddle()
        {
            x = y = 0;
        }
        cPaddle(int posx, int posy) : cPaddle()
        {
            originalx = posx;
            originaly = posy;
            x = posx;
            y = posy;
        }
        inline void Reset() { x = originalx; y = originaly;};
        inline int getX() {return x;};
        inline int gety() {return y;};
        inline void moveup() {y--;};
        inline void movedown() {y++;};
        friend ostream & operator << (ostream & o, cPaddle c)
        {
            o << "Paddle [" << c.x << "," << c.y << "]";
            return o;
        }
};

class cGameManager
{
private:
    int width, height;
    int score1, score2;
    char up1, down1, up2, down2;
    bool quit;
    cBall * ball;
    cPaddle * player1;
    cPaddle * player2;

public:
    cGameManager(int w, int h)
    {
        srand(time(NULL));
        quit = false;
        up1 = 'w'; up2 = 'i';
        down1 = 's'; down2 = 'k';
        score1 = score2 = 0;
        width = w; height = h;
        ball = new cBall(w / 2, h / 2);
        player1 = new cPaddle(1, h / 2 - 3);
        player2 = new cPaddle(w - 2, h / 2 - 3);
    }
    cGameManager()
    {
        delete ball, player1, player2;
    }
    void ScoreUp(cPaddle * player)
    {
        if (player == player1)
            score1++;
        else if (player == player2)
            score2++;

        ball->Reset();
        player1->Reset();
        player2->Reset();
    }
};

int main()
{
    cPaddle p1(0,0);
    cPaddle p2(10, 0);
    cout << p1 << endl;
    cout << p2 << endl;
    p1.moveup();
    p2.movedown();
    cout << p1 << endl;
    cout << p2 << endl;

    return 0;
}
