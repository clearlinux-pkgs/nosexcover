#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : nosexcover
Version  : 1.0.11
Release  : 38
URL      : http://pypi.debian.net/nosexcover/nosexcover-1.0.11.tar.gz
Source0  : http://pypi.debian.net/nosexcover/nosexcover-1.0.11.tar.gz
Summary  : Extends nose.plugins.cover to add Cobertura-style XML reports
Group    : Development/Tools
License  : BSD-3-Clause
Requires: nosexcover-python = %{version}-%{release}
Requires: nosexcover-python3 = %{version}-%{release}
Requires: coverage
Requires: nose
BuildRequires : buildreq-distutils3
BuildRequires : coverage
BuildRequires : nose

%description
--------------
        
        A companion to the built-in nose.plugins.cover, this plugin will write out an XML coverage report to a file named coverage.xml.

%package python
Summary: python components for the nosexcover package.
Group: Default
Requires: nosexcover-python3 = %{version}-%{release}

%description python
python components for the nosexcover package.


%package python3
Summary: python3 components for the nosexcover package.
Group: Default
Requires: python3-core
Provides: pypi(nosexcover)
Requires: pypi(coverage)
Requires: pypi(nose)

%description python3
python3 components for the nosexcover package.


%prep
%setup -q -n nosexcover-1.0.11
cd %{_builddir}/nosexcover-1.0.11

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1603397003
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
