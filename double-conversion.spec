#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : double-conversion
Version  : 3.1.5
Release  : 31
URL      : https://github.com/google/double-conversion/archive/v3.1.5/double-conversion-3.1.5.tar.gz
Source0  : https://github.com/google/double-conversion/archive/v3.1.5/double-conversion-3.1.5.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause
Requires: double-conversion-filemap = %{version}-%{release}
Requires: double-conversion-lib = %{version}-%{release}
Requires: double-conversion-license = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-scons

%description
https://github.com/google/double-conversion
This project (double-conversion) provides binary-decimal and decimal-binary
routines for IEEE doubles.

%package dev
Summary: dev components for the double-conversion package.
Group: Development
Requires: double-conversion-lib = %{version}-%{release}
Provides: double-conversion-devel = %{version}-%{release}
Requires: double-conversion = %{version}-%{release}

%description dev
dev components for the double-conversion package.


%package filemap
Summary: filemap components for the double-conversion package.
Group: Default

%description filemap
filemap components for the double-conversion package.


%package lib
Summary: lib components for the double-conversion package.
Group: Libraries
Requires: double-conversion-license = %{version}-%{release}
Requires: double-conversion-filemap = %{version}-%{release}

%description lib
lib components for the double-conversion package.


%package license
Summary: license components for the double-conversion package.
Group: Default

%description license
license components for the double-conversion package.


%prep
%setup -q -n double-conversion-3.1.5
cd %{_builddir}/double-conversion-3.1.5

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1634680117
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
%cmake .. -DBUILD_SHARED_LIBS:BOOL=ON -DINSTALL_LIB_DIR=/usr/lib64
make  %{?_smp_mflags}
popd
mkdir -p clr-build-avx2
pushd clr-build-avx2
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -Wl,-z,x86-64-v3 -ffat-lto-objects -flto=auto -march=x86-64-v3 -mtune=skylake "
export FCFLAGS="$FFLAGS -O3 -Wl,-z,x86-64-v3 -ffat-lto-objects -flto=auto -march=x86-64-v3 -mtune=skylake "
export FFLAGS="$FFLAGS -O3 -Wl,-z,x86-64-v3 -ffat-lto-objects -flto=auto -march=x86-64-v3 -mtune=skylake "
export CXXFLAGS="$CXXFLAGS -O3 -Wl,-z,x86-64-v3 -ffat-lto-objects -flto=auto -march=x86-64-v3 -mtune=skylake "
export CFLAGS="$CFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
export CXXFLAGS="$CXXFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
export FFLAGS="$FFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
export FCFLAGS="$FCFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
%cmake .. -DBUILD_SHARED_LIBS:BOOL=ON -DINSTALL_LIB_DIR=/usr/lib64
make  %{?_smp_mflags}
popd

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
cd clr-build; make test || :
cd ../clr-build-avx2;
make test || : || :

%install
export SOURCE_DATE_EPOCH=1634680117
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/double-conversion
cp %{_builddir}/double-conversion-3.1.5/COPYING %{buildroot}/usr/share/package-licenses/double-conversion/8d434c9c1704b544a8b0652efbc323380b67f9bc
cp %{_builddir}/double-conversion-3.1.5/LICENSE %{buildroot}/usr/share/package-licenses/double-conversion/8d434c9c1704b544a8b0652efbc323380b67f9bc
pushd clr-build-avx2
%make_install_v3  || :
popd
pushd clr-build
%make_install
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot}/usr/share/clear/optimized-elf/ %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/double-conversion/bignum.h
/usr/include/double-conversion/cached-powers.h
/usr/include/double-conversion/diy-fp.h
/usr/include/double-conversion/double-conversion.h
/usr/include/double-conversion/fast-dtoa.h
/usr/include/double-conversion/fixed-dtoa.h
/usr/include/double-conversion/ieee.h
/usr/include/double-conversion/strtod.h
/usr/include/double-conversion/utils.h
/usr/lib64/cmake/double-conversion/double-conversionConfig.cmake
/usr/lib64/cmake/double-conversion/double-conversionConfigVersion.cmake
/usr/lib64/cmake/double-conversion/double-conversionTargets-relwithdebinfo.cmake
/usr/lib64/cmake/double-conversion/double-conversionTargets.cmake
/usr/lib64/libdouble-conversion.so

%files filemap
%defattr(-,root,root,-)
/usr/share/clear/filemap/filemap-double-conversion

%files lib
%defattr(-,root,root,-)
/usr/lib64/libdouble-conversion.so.3
/usr/lib64/libdouble-conversion.so.3.1.5
/usr/share/clear/optimized-elf/lib*

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/double-conversion/8d434c9c1704b544a8b0652efbc323380b67f9bc
