import numpy as np
import cv2

poly_vertices=[] # for polygon vertices
xx=0 # mouse pointer position's X-Coordinate
yy=0 # mouse pointer position's Y-Coordinate

def show_poly(frame,vertices,color = (255,255,0)): 
    # displays a polygon on the frame given the vertices 
    
    return cv2.fillPoly(frame.copy(),[vertices],color=color)
    
def add_image_alpha(image,frame,alpha=0.5): 
    # add image over the other frame with a specfic opacity
    # frame and image must be of shape
    
    return cv2.addWeighted(image.copy(),alpha,frame.copy(),1-alpha,0)
    
def show_coord(frame,x,y,font = cv2.FONT_HERSHEY_SIMPLEX,fontScale = 1,thickness = 2,
               color=(255,0,0),radius=4,flag=True,fill=-1,offset=(1,1)): 
   # displays coordinates (x,y) on the frame
   # flag if true also marks the coordinate by a circle of default radius 4
               
    copy = frame.copy()
    cv2.circle(copy,(x,y),radius,color,fill)
    if flag:
        return cv2.putText(copy,f'({x},{y})',(x+offset[0],y+offset[1]),font,
                fontScale,color,thickness,cv2.LINE_AA)
    else:
        return copy
        
def add_vertices(frame,vertices,color=(0,0,255),radius=4,flag=True,fill=-1,offset=(1,1)):
    # array of coordinates(vertices) are displayed on the frame(input image)
    
    frame_dup = frame.copy()
    for i in vertices:
         frame_dup = show_coord(frame_dup,i[0],i[1],color=color,
                                radius=radius,flag=flag,fill=fill,offset=offset)
    return frame_dup

def get_coord(event,x,y,flags,params): 
    # double click left mouse button (LMB) to store the current coordinates of mouse pointer in poly_vertices
    # double click right mouse button (RMB) to pop the last coordinates of stored in poly_vertices
        
    global xx,yy,poly_vertices
    xx = x
    yy = y
    if event == cv2.EVENT_LBUTTONDBLCLK:
        poly_vertices.append((xx,yy))
    elif event == cv2.EVENT_RBUTTONDBLCLK:
        poly_vertices.pop()