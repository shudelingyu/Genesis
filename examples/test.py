import glfw
from OpenGL.GL import *
from OpenGL.GL import shaders
import sys

def is_extension_supported(extension):
    # 获取所有扩展
    extensions = glGetString(GL_EXTENSIONS).decode('utf-8').split()
    return extension in extensions

def main():
    # 初始化 glfw
    if not glfw.init():
        print("Failed to initialize GLFW")
        sys.exit()

    # 创建窗口
    window = glfw.create_window(800, 600, "OpenGL Extension Check", None, None)
    if not window:
        glfw.terminate()
        print("Failed to create GLFW window")
        sys.exit()

    glfw.make_context_current(window)

    # 检查扩展是否支持
    extension = "texture_filter_anisotropic"
    if is_extension_supported(extension):
        print(f"{extension} is supported!")
    else:
        print(f"{extension} is NOT supported.")

    # 查询各向异性最大级别（如果支持）
    if extension in glGetString(GL_EXTENSIONS).decode('utf-8'):
        max_anisotropy = glGetIntegerv(GL_MAX_TEXTURE_MAX_ANISOTROPY_EXT)
        print(f"Max anisotropy: {max_anisotropy}")

    glfw.terminate()

if __name__ == "__main__":
    main()