{ pkgs }: {
  deps = [
    pkgs.python39
    pkgs.python39Packages.pip
    pkgs.python39Packages.virtualenv
    pkgs.cmake
    pkgs.pkg-config
    pkgs.opencv
    pkgs.dlib
    pkgs.boost
    pkgs.eigen
    pkgs.gcc
    pkgs.make
    pkgs.git
    pkgs.ffmpeg
    pkgs.libjpeg
    pkgs.libpng
    pkgs.zlib
    pkgs.openssl
    pkgs.curl
    pkgs.wget
    pkgs.unzip
  ];
} 