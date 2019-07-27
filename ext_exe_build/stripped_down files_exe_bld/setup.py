from setuptools import setup

# setup(name='extract_exe_build',
#       version='0.1.0',
#       packages=['extract_exe_build'],
#       include_package_data=True,
#       entry_points={
#           # 'console_scripts': [
#           'gui_scripts': [
#               'extract_exe_build = extract_exe_build.__main__:main'
#           ]
#       },
#       )

setup(name='extract_exe_build',
      version='0.1.0',
      packages=['extract_exe_build'],
      include_package_data=True,
      # install_requires=["extract_exe_build.extraction_tool"],
      entry_points={
          # 'console_scripts': [
          'gui_scripts': [
              'extract_exe_build = extract_exe_build.__main__:main'
          ]
      },
      )

# You must use setuptools, otherwise this won’t work.
# The most important piece of code is the entry_points declaration (unsurprisingly).
# The declaration reads

# "name_of_executable = module.with:function_to_execute"

# If you are developing a GUI application (in Tkinter,
# PyQt/PySide, wxPython, PyGTK, PyGame…), you should
# change the declaration to gui_scripts. On *nix,
# this makes no difference, but on Windows, it means
# that running your script by opening the created
# .exe files does not show a console window. Note
# that stdout/stderr do not work in that mode under
# Windows, which can lead to spurious application
# crashes. (GUI-only processes cannot use stdout/stderr
# because they don’t have a console attached).
#
# You can create multiple scripts this way. You can
# also have multiple console_scripts and gui_scripts
# in one setup file.
