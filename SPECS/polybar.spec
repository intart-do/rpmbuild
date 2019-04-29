Name: polybar
Version: 3.3.1
Release: 1
Summary: A fast and easy-to-use tool for creating status bars.
Source: https://github.com/jaagr/polybar/releases/download/3.3.1/%{name}-%{version}.tar

License: MIT
URL: https://github.com/jaagr/polybar

BuildRequires: alsa-lib-devel
BuildRequires: pulseaudio-libs-devel
BuildRequires: binutils
BuildRequires: cairo-devel
BuildRequires: clang
BuildRequires: cmake
BuildRequires: cmake-data
BuildRequires: git
BuildRequires: i3
BuildRequires: jsoncpp-devel
BuildRequires: libcurl-devel
BuildRequires: libmpdclient-devel
BuildRequires: libxcb-devel
BuildRequires: python2
BuildRequires: wireless-tools-devel
BuildRequires: xcb-proto
BuildRequires: xcb-util-image-devel
BuildRequires: xcb-util-wm-devel
BuildRequires: xcb-util-xrm-devel
Requires: cairo
Requires: jsoncpp
Requires: libxcb
Requires: python2
Requires: xcb-proto
Requires: xcb-util-image
Requires: xcb-util-wm
Requires: xcb-util-xrm

%description
A fast and easy-to-use tool for creating status bars.

%prep
%autosetup -n polybar

%build
mkdir build
cd build
cmake .. -DCMAKE_C_COMPILER="clang" -DCMAKE_CXX_COMPILER="clang++" -DENABLE_ALSA:BOOL="ON" -DENABLE_I3:BOOL="ON" -DENABLE_MPD:BOOL="ON" -DENABLE_NETWORK:BOOL="ON" -DENABLE_CURL:BOOL="ON"
make

%install
%make_install
%check

%files
/usr/local/bin/polybar
/usr/local/bin/polybar-msg
/usr/local/share/doc/polybar/config
/usr/local/share/man/man1/polybar.1
/usr/local/share/zsh/site-functions/_polybar
/usr/local/share/zsh/site-functions/_polybar_msg
/usr/local/share/bash-completion/completions/polybar

%changelog
* Fri Apr 13 2018 geoffbeier <geoffbeier@gmail.com> 3.1.0-4
- update to 3.1.0

* Mon Apr 10 2017 notkild <notkild@gmail.com> 3.0.5-3
- 

* Mon Apr 10 2017 notkild <notkild@gmail.com>
- 

* Mon Apr 10 2017 notkild <notkild@gmail.com> 3.0.5-2
-

* Mon Apr 10 2017 notkild <notkild@gmail.com>
-

* Mon Apr 10 2017 notkild <notkild@gmail.com> 3.0.5-1
- new package built with tito

* Mon Apr 10 2017 notkild <notkild@gmail.com>
-

* Mon Apr 10 2017 notkild <notkild@gmail.com>
-

* Mon Apr 10 2017 notkild <notkild@gmail.com> 3.0.5-1
-

* Mon Apr 10 2017 notkild <notkild@gmail.com>
-

* Mon Apr 10 2017 notkild <notkild@gmail.com> 3.0.6-1
- new package built with tito

