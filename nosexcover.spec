#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : nosexcover
Version  : 1.0.11
Release  : 17
URL      : http://pypi.debian.net/nosexcover/nosexcover-1.0.11.tar.gz
Source0  : http://pypi.debian.net/nosexcover/nosexcover-1.0.11.tar.gz
Summary  : Extends nose.plugins.cover to add Cobertura-style XML reports
Group    : Development/Tools
License  : BSD-3-Clause
Requires: nosexcover-python
BuildRequires : coverage
BuildRequires : nose
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools

%description
nose-xmlcover
--------------
A companion to the built-in nose.plugins.cover, this plugin will write out an XML coverage report to a file named coverage.xml.

%package python
Summary: python components for the nosexcover package.
Group: Default

%description python
python components for the nosexcover package.


%prep
%setup -q -n nosexcover-1.0.11

%build
export LANG=C
python2 setup.py build -b py2
python3 setup.py build -b py3

%install
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot}
python3 -tt setup.py build -b py3 install --root=%{buildroot}

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
