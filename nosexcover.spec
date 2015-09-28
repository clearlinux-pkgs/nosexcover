#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : nosexcover
Version  : 1.0.10
Release  : 8
URL      : https://pypi.python.org/packages/source/n/nosexcover/nosexcover-1.0.10.tar.gz
Source0  : https://pypi.python.org/packages/source/n/nosexcover/nosexcover-1.0.10.tar.gz
Summary  : Extends nose.plugins.cover to add Cobertura-style XML reports
Group    : Development/Tools
License  : BSD-3-Clause
Requires: nosexcover-python
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools

%description
No detailed description available

%package python
Summary: python components for the nosexcover package.
Group: Default

%description python
python components for the nosexcover package.


%prep
%setup -q -n nosexcover-1.0.10

%build
python2 setup.py build -b py2
python3 setup.py build -b py3

%install
rm -rf %{buildroot}
python2 setup.py build -b py2 install --root=%{buildroot}
python3 setup.py build -b py3 install --root=%{buildroot}

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
