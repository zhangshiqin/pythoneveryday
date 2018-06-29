## 1.TCL/TK的版本问题

macos10.9以后且python版本为64位的，不再需要使用IDLE或者tkinter，因为有了内置的Tcl/Tk 8.6

`If you are using Python from a python.org 64-bit-only Python installer for macOS 10.9 and later,`

no further action is needed to use IDLE or tkinter. A built-in version of Tcl/Tk 8.6 will be used.

`If you are using Python from a python.org 64-bit/32-bit Python installer for macOS 10.6 and later,`

you should only use IDLE or tkinter with an updated third-party Tcl/Tk 8.5 (not 8.6), like ActiveTcl 8.5 installed.

`If you are using macOS 10.6, do not use IDLE or Tkinter from the Apple-supplied Python 2.6.1 in macOS 10.6.`

If possible, install and use a newer version of Python and of Tcl/Tk.

If you are using macOS 10.7 or later, the Apple-supplied Tcl/Tk 8.5 still has serious bugs that can cause application
crashes.

If you wish to use IDLE or Tkinter, install and use a newer version of Python and of Tcl/Tk.

Python's integrated development environment, IDLE, and the tkinter GUI toolkit it uses, depend on the Tk GUI toolkit
which is not part of Python itself.

For best results, it is important that the proper release of Tcl/Tk is installed on your machine.

For recent Python installers for macOS downloadable from this website, here is a summary of current recommendations
followed by more detailed information.

```
Aqua Cocoa Tk

A newer native implementation available as a universal 64-bit and 32-bit binary.
This variant is the standard native macOS variant in Tk 8.6 and as of Tk 8.5.13.
Aqua Cocoa support was backported to Tk 8.5 (prior to 8.5.13) and released by Apple starting with macOS 10.6 and by
ActiveState starting with their 8.5.9.1 release.
```

```
Tcl/Tk Releases
built-in 8.6.8
64-bit-only (and all 3.7.x) Python installers for macOS downloadable from python.org supply their own private copies of
Tcl/Tk 8.6.8.
**They do not look for or use any third-party or system copies of Tcl/Tk.**
This is an Aqua Cocoa Tk.
```


## pyinstaller

[https://pythonhosted.org/PyInstaller/when-things-go-wrong.html](https://pythonhosted.org/PyInstaller/when-things-go-wrong.html)

```
usage: pyinstaller [-h] [-v] [-D] [-F] [--specpath DIR] [-n NAME]
                   [--add-data <SRC;DEST or SRC:DEST>]
                   [--add-binary <SRC;DEST or SRC:DEST>] [-p DIR]
                   [--hidden-import MODULENAME]
                   [--additional-hooks-dir HOOKSPATH]
                   [--runtime-hook RUNTIME_HOOKS] [--exclude-module EXCLUDES]
                   [--key KEY] [-d] [-s] [--noupx] [-c] [-w]
                   [-i <FILE.ico or FILE.exe,ID or FILE.icns>]
                   [--version-file FILE] [-m <FILE or XML>] [-r RESOURCE]
                   [--uac-admin] [--uac-uiaccess] [--win-private-assemblies]
                   [--win-no-prefer-redirects]
                   [--osx-bundle-identifier BUNDLE_IDENTIFIER]
                   [--runtime-tmpdir PATH] [--distpath DIR]
                   [--workpath WORKPATH] [-y] [--upx-dir UPX_DIR] [-a]
                   [--clean] [--log-level LEVEL]
                   scriptname [scriptname ...]
```

### warn.txt文件中发现了很多缺失的模块

When the `Analysis` step runs, it produces error and warning messages. These display after the command line if the
`--log-level` option allows it. Analysis also puts messages in a warnings file named `build/name/warnname.txt` in the
work-path= directory.

Analysis creates a message when it detects an import and the module it names cannot be found. A message may also be
produced when a class or function is declared in a package (an __init__.py module), and the import specifies `package.name.`
In this case, the analysis can’t tell if name is supposed to refer to a submodule or package.

The “module not found” messages are not classed as errors because typically there are many of them. For example, many
standard modules conditionally import modules for different platforms that may or may not be present.

All “module not found” messages are written to the `build/name/warnname.txt` file. They are not displayed to standard
output because there are many of them. Examine the warning file; often there will be dozens of modules not found, but
**their absence has no effect**.

When you run the bundled app and it terminates with an ImportError, that is the time to examine the warning file. Then
see Helping PyInstaller Find Modules below for how to proceed.

