import glfw
from glfw.GLFW import GLFW_KEY_ENTER,GLFW_KEY_W,GLFW_KEY_S,GLFW_KEY_A,\
    GLFW_KEY_D,GLFW_KEY_Q,GLFW_KEY_E, GLFW_KEY_UP,GLFW_KEY_DOWN,GLFW_KEY_RIGHT,GLFW_KEY_LEFT
from OpenGL.GL import *
from OpenGL.GL.shaders import compileProgram, compileShader
import pyrr
from GameEngine.TextureLoader import load_texture
from GameEngine.ObjLoader import ObjLoader
from GameEngine.GUI import Gui
vertex_src = """
# version 330

layout(location = 0) in vec3 a_position;
layout(location = 1) in vec2 a_texture;
layout(location = 2) in vec3 a_normal;

uniform mat4 model;
uniform mat4 projection;
uniform mat4 view;

out vec2 v_texture;

void main()
{
    gl_Position = projection * view * model * vec4(a_position, 1.0);
    v_texture = a_texture;
}
"""

fragment_src = """
# version 330

in vec2 v_texture;

out vec4 out_color;

uniform sampler2D s_texture;

void main()
{
    out_color = texture(s_texture, v_texture);
}
"""
poc_x = 0
poc_y = 0
poc_z = 0

Rot_x = 1
Rot_y = 1
Rot_z = 1

Rot_Selete = 0

# glfw callback functions
def window_resize(window, width, height):
    glViewport(0, 0, width, height)
    projection = pyrr.matrix44.create_perspective_projection_matrix(45, width / height, 0.1, 100)
    glUniformMatrix4fv(proj_loc, 1, GL_FALSE, projection)


# initializing glfw library
if not glfw.init():
    raise Exception("glfw can not be initialized!")
timer1 = glfw.get_time()


def on_key(windowp, key, scancode, action, mods):
    global poc_z,poc_x,poc_y,Rot_z,Rot_x,Rot_y,Rot_Selete
    if key == GLFW_KEY_ENTER:
        glfw.set_window_should_close(windowp,1)
    # set viewport
    if key == GLFW_KEY_W:
        poc_z -= 0.1
    if key == GLFW_KEY_S:
        poc_z += 0.1
    if key == GLFW_KEY_A:
        poc_x -= 0.1
    if key == GLFW_KEY_D:
        poc_x += 0.1
    if key == GLFW_KEY_Q:
        poc_y += 0.1
    if key == GLFW_KEY_E:
        poc_y -= 0.1
    # set rot
    if key == GLFW_KEY_UP:
        Rot_y += 0.1
        Rot_Selete = 1
    if key == GLFW_KEY_DOWN:
        Rot_y -= 0.1
        Rot_Selete = 1
    if key == GLFW_KEY_RIGHT:
        Rot_y +=0.1
        Rot_Selete = 2
    if key == GLFW_KEY_LEFT:
        Rot_y -=0.1
        Rot_Selete = 2



# creating the window
window = glfw.create_window(1280, 720, "My OpenGL window", None, None)

# check if window was created
if not window:
    glfw.terminate()
    raise Exception("glfw window can not be created!")

# set window's position
glfw.set_window_pos(window, 400, 200)

# set the callback function for window resize
glfw.set_window_size_callback(window, window_resize)

# make the context current
glfw.make_context_current(window)

# load here the 3d meshes
chibi_indices, chibi_buffer = ObjLoader.load_model("Bin/Grassv2.obj")
# monkey_indices, monkey_buffer = ObjLoader.load_model("meshes/monkey.obj")

shader = compileProgram(compileShader(vertex_src, GL_VERTEX_SHADER), compileShader(fragment_src, GL_FRAGMENT_SHADER))

# VAO and VBO
VAO = glGenVertexArrays(2)
VBO = glGenBuffers(2)
# EBO = glGenBuffers(1)

# Chibi VAO
glBindVertexArray(VAO[0])
# Chibi Vertex Buffer Object
glBindBuffer(GL_ARRAY_BUFFER, VBO[0])
glBufferData(GL_ARRAY_BUFFER, chibi_buffer.nbytes, chibi_buffer, GL_STATIC_DRAW)

# glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, EBO)
# glBufferData(GL_ELEMENT_ARRAY_BUFFER, chibi_indices.nbytes, chibi_indices, GL_STATIC_DRAW)

# chibi vertices
glEnableVertexAttribArray(0)
glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, chibi_buffer.itemsize * 8, ctypes.c_void_p(0))
# chibi textures
glEnableVertexAttribArray(1)
glVertexAttribPointer(1, 2, GL_FLOAT, GL_FALSE, chibi_buffer.itemsize * 8, ctypes.c_void_p(12))
# chibi normals
glVertexAttribPointer(2, 3, GL_FLOAT, GL_FALSE, chibi_buffer.itemsize * 8, ctypes.c_void_p(20))
glEnableVertexAttribArray(2)

# Monkey VAO
# glBindVertexArray(VAO[1])
# # Monkey Vertex Buffer Object
# glBindBuffer(GL_ARRAY_BUFFER, VBO[1])
# glBufferData(GL_ARRAY_BUFFER, monkey_buffer.nbytes, monkey_buffer, GL_STATIC_DRAW)
#
# # monkey vertices
# glEnableVertexAttribArray(0)
# glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, monkey_buffer.itemsize * 8, ctypes.c_void_p(0))
# # monkey textures
# glEnableVertexAttribArray(1)
# glVertexAttribPointer(1, 2, GL_FLOAT, GL_FALSE, monkey_buffer.itemsize * 8, ctypes.c_void_p(12))
# # monkey normals
# glVertexAttribPointer(2, 3, GL_FLOAT, GL_FALSE, monkey_buffer.itemsize * 8, ctypes.c_void_p(20))
# glEnableVertexAttribArray(2)


textures = glGenTextures(2)
load_texture("Bin/Grass.png", textures[0])
# load_texture("meshes/monkey.jpg", textures[1])

glUseProgram(shader)
glClearColor(1, 1, 1, 1)
glEnable(GL_DEPTH_TEST)
glEnable(GL_BLEND)
glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

projection = pyrr.matrix44.create_perspective_projection_matrix(45, 1280 / 720, 0.1, 100)
chibi_pos = pyrr.matrix44.create_from_translation(pyrr.Vector3([poc_x, poc_y,poc_z]))
# monkey_pos = pyrr.matrix44.create_from_translation(pyrr.Vector3([-4, 0, 0]))

# eye, target, up
view = pyrr.matrix44.create_look_at(pyrr.Vector3([0, 0, 8]), pyrr.Vector3([0, 0, 0]), pyrr.Vector3([0, 1, 0]))

model_loc = glGetUniformLocation(shader, "model")
proj_loc = glGetUniformLocation(shader, "projection")
view_loc = glGetUniformLocation(shader, "view")

glUniformMatrix4fv(proj_loc, 1, GL_FALSE, projection)
glUniformMatrix4fv(view_loc, 1, GL_FALSE, view)

# Install a key handler
glfw.set_key_callback(window, on_key)
# the main application loop
timer2 = glfw.get_time()
timer1 = timer2 - timer1
print(timer1)
while not glfw.window_should_close(window):

    # Rot_y = 0
    glfw.poll_events()
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    chibi_pos = pyrr.matrix44.create_from_translation(pyrr.Vector3([poc_x, poc_y, poc_z]))
    if(Rot_Selete == 1):
        rot_y = pyrr.Matrix44.from_x_rotation(Rot_y)
    else:
        rot_y = pyrr.Matrix44.from_y_rotation(Rot_y)
    model = pyrr.matrix44.multiply(rot_y, chibi_pos)

    # model = pyrr.matrix44.multiply(rot_x,chibi_pos)

    # draw the chibi character
    glBindVertexArray(VAO[0])
    glBindTexture(GL_TEXTURE_2D, textures[0])
    glUniformMatrix4fv(model_loc, 1, GL_FALSE, model)

    glDrawArrays(GL_TRIANGLES, 0, len(chibi_indices))

    # glDrawElements(GL_TRIANGLES, len(chibi_indices), GL_UNSIGNED_INT, None)
    #
    # rot_y = pyrr.Matrix44.from_y_rotation(-0.8 * glfw.get_time())
    # model = pyrr.matrix44.multiply(rot_y, monkey_pos)
    #
    # # draw the monkey head
    # glBindVertexArray(VAO[1])
    # glBindTexture(GL_TEXTURE_2D, textures[1])
    # glUniformMatrix4fv(model_loc, 1, GL_FALSE, model)
    # glDrawArrays(GL_TRIANGLES, 0, len(monkey_indices))
    # print(poc_x,poc_y,poc_z,Rot_y)
    Gui.gui_showFPS()
    glfw.swap_buffers(window)

# terminate glfw, free up allocated resources
glfw.terminate()