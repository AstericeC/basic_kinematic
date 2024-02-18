import matplotlib.pyplot as plt
import numpy as np
import time
import os

leg1 = 3
leg2 = 3
class algorithm():
    def __init__():
        print('test algorithm')        
    # circle
    def plot_circle(r):
        angles = np.linspace(0 * np.pi, 2 * np.pi, 100) 
        xs = np.cos(angles)*r
        ys = np.sin(angles)*r
        plt.plot(xs, ys, color = 'green')
        plt.gca().set_aspect('equal')
        plt.plot(xs,ys)
        
    def convert_deg_to_rad(dataIn):
        return dataIn*np.pi/180
    
    def convert_rad_to_deg(dataIn):
        return dataIn*180/np.pi
        
    def check_length(datax, datay):
        leg1 = datax
        leg2 = datay
        conversion = np.sqrt(leg1*leg1 + leg2*leg2)
        return conversion
        
    def algorithm_x(x): # dataIn is float y axis
        a = leg1
        b = leg2
        c = x
        
        #law cosine
        # cos a = (b2+c2 -a2)/2bc
        if c == 0:
            angleA = 0
        else:
            angleA = np.arccos((b*b + c*c - a*a)/(2*b*c))
        
        #  angle compensation such that it zero with the x1y1 end effector
        compensator = 3.142 - angleA
        
        # sine law
        # (sin A/ a) = (sin B/b) = (sin C/c)
        # (sin C)/c = (sin A) / a
        # sin C = c * sin A / a
        angleC = np.arcsin(c*np.sin(angleA)/a)
        
        # base angle compensator
        angleA = angleA + 3.142/2
        angleC = angleC + 3.142/2
        
        x1 = (np.cos(angleA)*leg1)
        y1 = (np.sin(angleA)*leg1)
        
        x2 = (np.cos(compensator - angleC)*leg2 + x1)
        y2 = (np.sin(- compensator + angleC)*leg2 + y1)
       
        xs = [0,x1,x2]
        ys = [0,y1,y2]
        
        # print(f'x1: {x1} y1 {y1} | x2: {x2}  y2: {y2}')
        print(f'angle A: {algorithm.convert_rad_to_deg(angleA)} angleB: {algorithm.convert_rad_to_deg(3.142-angleA-angleC)} angleC: {algorithm.convert_rad_to_deg(angleC)}')
        print(f'length {round(x2)}')
        # algorithm.end_effector_check(x2,y2)        
        plt.plot(xs,ys,'x')
        plt.plot(xs,ys,'-')
        
        plt.pause(0.1)
        
    def algorithm_xy(x,y): # dataIn is float y axis
        
        # calculate y
        length = np.sqrt(x*x + y*y) # length between end effector and base
        y_angle_compensate = np.arctan(x/y)
        a = leg1
        b = leg2
        c = length
        
        #law cosine
        # cos a = (b2+c2 -a2)/2bc
        if c == 0:
            angleA = 0
        else:
            angleA = np.arccos((b*b + c*c - a*a)/(2*b*c))
        
        #  angle compensation such that it zero with the x1y1 end effector
        compensator = 3.142 - angleA
        
        # sine law
        # (sin A/ a) = (sin B/b) = (sin C/c)
        # (sin C)/c = (sin A) / a
        # sin C = c * sin A / a
        angleC = np.arcsin(c*np.sin(angleA)/a)
        
        # base angle compensator
        # angleA = angleA + 3.142/2
        # angleC = angleC + 3.142/2
        angleA = angleA + y_angle_compensate
        angleC = angleC + y_angle_compensate
        
        x1 = (np.cos(angleA)*leg1)
        y1 = (np.sin(angleA)*leg1)
        
        x2 = (np.cos(compensator - angleC)*leg2 + x1)
        y2 = (np.sin(- compensator + angleC)*leg2 + y1)
       
        xs = [0,x1,x2]
        ys = [0,y1,y2]
        
        # print(f'x1: {x1} y1 {y1} | x2: {x2}  y2: {y2}')
        print(f'angle A: {algorithm.convert_rad_to_deg(angleA)} angleB: {algorithm.convert_rad_to_deg(3.142-angleA-angleC)} angleC: {algorithm.convert_rad_to_deg(angleC)}')
        print(f'x: {(x2)} y: {y2}')
        # algorithm.end_effector_check(x2,y2)        
        plt.plot(xs,ys,'x')
        plt.plot(xs,ys,'-')
        
        plt.pause(0.1)
        
        
def main():    
    os.system("cls")
    algorithm.plot_circle(6)
    # algorithm.test_stuff(1.047)
    # algorithm.algorithm(0)
    # time.sleep(0.5)
    # algorithm.algorithm(1)
    # time.sleep(0.5)
    # algorithm.algorithm(1)
    # for i in range(4):
    #     print(f'index: {i}')
    #     algorithm.algorithm_x(i)
            
    #     time.sleep(0.5)
    algorithm.algorithm_xy(2,2)
    algorithm.algorithm_xy(2,1)
    plt.show()


        
        
        
            
    
if __name__ == "__main__":
    main()