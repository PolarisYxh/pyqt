from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from src.third import *
from OpenGL.GL import *
from OpenGL.GLUT import *
import OpenGL.GL.shaders as shad
from OpenGL.arrays import vbo
from PyQt5.QtOpenGL import *
import numpy as np

class OpenGLwidget(QOpenGLWidget):

    VBO = 0
    VAO = 0
    EBO = 0
    #Shader_Program = glCreateProgram()
    shaderCube = QOpenGLShaderProgram()
    # 顶点着色器部分
    VERTEX_SHADER = """   
    #version 330
    layout (location = 0) in vec3 Position;
    void main()
    {
        gl_Position = vec4(Position.x,  Position.y, Position.z, 1.0);
    }
    """


    # 片段着色器部分,字符串类型
    FRAGMENT_SHADER = """ 
    #version 330
    out vec4 FragColor;
    void main()
    {
        FragColor = vec4(0.0, 1.0, 1.0, 1.0);
    }
    """
    def __init__(self):
        super(OpenGLwidget, self).__init__()
        format = QSurfaceFormat()
        format.setRenderableType(QSurfaceFormat.OpenGL)
        format.setProfile(QSurfaceFormat.CoreProfile)
        format.setVersion(3, 3)
        self.setFormat(format)

    def initializeGL(self):
        #QOpenGLFunctions.initializeOpenGLFunctions()
        glClearColor(0, 0, 1, 1)
        glEnable(GL_DEPTH_TEST)
        '''glEnable(GL_LIGHT0)
        glEnable(GL_LIGHTING)
        glColorMaterial(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE)
        glEnable(GL_COLOR_MATERIAL)'''
        #self.Compile_Shader()
        self.shaderCube.addShaderFromSourceCode(QOpenGLShader.Vertex, self.VERTEX_SHADER)
        self.shaderCube.addShaderFromSourceCode(QOpenGLShader.Fragment, self.FRAGMENT_SHADER);
        #self.shaderCube.addShaderFromSourceFile(QOpenGLShader.Fragment, "shader/simple.frag");
        self.shaderCube.link()
        self.CreateBuffer()

    '''def Create_Shader(self, ShaderProgram, Shader_Type, Source):  # 创建并且添加着色器（相当于AddShader）Shader_Type为类型
        ShaderObj = glCreateShader(Shader_Type)  # 创建Shader对象
        glShaderSource(ShaderObj, Source)
        glCompileShader(ShaderObj)  # 进行编译
        glAttachShader(ShaderProgram, ShaderObj)  # 将着色器对象关联到程序上

    def Compile_Shader(self):  # 编译着色器
        Shader_Program = glCreateProgram()  # 创建空的着色器程序
        self.Create_Shader(Shader_Program, GL_VERTEX_SHADER, self.VERTEX_SHADER)
        self.Create_Shader(Shader_Program, GL_FRAGMENT_SHADER, self.FRAGMENT_SHADER)
        glLinkProgram(Shader_Program)
        glUseProgram(Shader_Program)'''

    '''def Compile_Shader(self):  # 编译着色器
        vertex_shader = shad.compileShader("""#version 120
                void main() {
                    gl_Position =  gl_Vertex;
                }""", GL_VERTEX_SHADER)
        fragment_shader = shad.compileShader("""#version 120
                void main() {
                    gl_FragColor = vec4( 1, 1, 0, 1 );
                }""", GL_FRAGMENT_SHADER)
        self.shader = shad.compileProgram(vertex_shader, fragment_shader)'''

    def CreateBuffer(self):
        vertex = np.array([[-0.5, -0.5, 0.0],
                           [0.5, -0.5, 0.0],
                           [0.0, 0.5, 0.0]], dtype="float32")  # 创建顶点数组
        indices = np.array((0, 1, 2))
        self.VBO = vbo.VBO(vertex)
        self.EBO = vbo.VBO(indices, target=GL_ELEMENT_ARRAY_BUFFER)
        '''self.VAO = glGenVertexArrays(1)
        self.VBO = glGenBuffers(1)  # 创建缓存
        self.EBO = glGenBuffers(1)

        glBindVertexArray(self.VAO)

        glBindBuffer(GL_ARRAY_BUFFER, self.VBO)  # 绑定
        #print(vertex.nbytes)
        glBufferData(GL_ARRAY_BUFFER, vertex.nbytes , vertex, GL_STATIC_DRAW)  # 输入数据

        glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, self.EBO)  # 绑定
        glBufferData(GL_ELEMENT_ARRAY_BUFFER, indices.nbytes, indices, GL_STATIC_DRAW)  # 输入数据
        #print(indices.nbytes)
        glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 12, 0)
        glEnableVertexAttribArray(0)

        glBindBuffer(GL_ARRAY_BUFFER, 0)  # 解绑
        glBindVertexArray(0)'''
        print("3333")

    def paintGL(self):
        print("4444")
        glClearColor(0.2, 0.3, 0.3, 1.0)
        glClear(GL_COLOR_BUFFER_BIT)
        self.update()
        #self.updateGL()
        #glUseProgram(self.Shader_Program)
        self.shaderCube.bind()
        self.VBO.bind()
        glInterleavedArrays(GL_N3F_V3F, 0, None)
        self.EBO.bind()
        #glBindVertexArray(self.VAO)
        glDrawElements(GL_TRIANGLES, 3, GL_UNSIGNED_INT, 0)
        #glFlush()
        #glBindVertexArray(0)


    def mypaintGL(self):
        for i in range(1, 1000):
            self.paintGL()


class third_(QWidget,Ui_Form):
    def __init__(self,parent=None):
        super(third_,self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle('third')
        self.center()
        '''self.initializeGL()
        self.paintGL()'''
        #self.openGLWidget.paintGL(self.paintGL)
        #elf.openGLWidget.initializeGL(self.initializeGL)
        self.openGLWidget = OpenGLwidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.openGLWidget.sizePolicy().hasHeightForWidth())
        self.openGLWidget.setSizePolicy(sizePolicy)
        self.horizontalLayout_3.addWidget(self.openGLWidget)
        self.pushButton_2.clicked.connect(self.openGLWidget.mypaintGL)

    def center(self):
        scr = QDesktopWidget().screenGeometry()
        size = self.geometry()
        # Qsize.
        self.move((scr.width() - size.width()) / 2, (scr.height() - size.height()) / 2)
        # self.move()
'''
    def initializeGL(self):
        print('1111')
        glClearColor(1, 0, 0, 1)
        glEnable(GL_DEPTH_TEST)
        glEnable(GL_LIGHT0)
        glEnable(GL_LIGHTING)
        glColorMaterial(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE)
        glEnable(GL_COLOR_MATERIAL)

    def paintGL(self):
        print('2222')
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glBegin(GL_TRIANGLES)
        glColor3f(1.0, 0.0, 0.0)
        glVertex3f(-0.5, -0.5, 0)
        glColor3f(0.0, 1.0, 0.0)
        glVertex3f(0.5, -0.5, 0)
        glColor3f(0.0, 0.0, 1.0)
        glVertex3f(0.0, 0.5, 0)
        glEnd()

'''