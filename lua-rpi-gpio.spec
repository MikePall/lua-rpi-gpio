Name:       lua-rpi-gpio
Version:    0.0.1
Release:    1%{?dist}
Summary:    Lua module providing an interface to Raspberry Pi GPIO
License:    MIT
URL:        https://github.com/craigbarnes/luajit-rpi-gpio
BuildArch:  noarch
Requires:   luajit
Source0:    gpio.lua

%description
This module makes use of the LuaJIT FFI library and hence requires
LuaJIT instead of the standard Lua distribution.


%prep
cp %{SOURCE0} %{_builddir}


%install
rm -rf %{buildroot}
install -Dpm644 gpio.lua %{buildroot}%{_datadir}/lua/5.1/rpi/gpio.lua


%files
%dir %{_datadir}/lua/5.1/rpi
%{_datadir}/lua/5.1/rpi/gpio.lua


%changelog

* Tue May 01 2012 Craig Barnes <cr@igbarn.es> - 0.0.1-1
- Initial package

