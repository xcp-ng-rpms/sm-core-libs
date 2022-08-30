%global package_speccommit cbbaa0098ff2aa9141c5967d0e1bafc5296abc73
%global package_srccommit v0.13.1

Name:    sm-core-libs
Version: 0.13.1
Release: 1%{?xsrel}%{?dist}
Summary: sm core libraries - SM common core libraries.

License:        LGPL
URL:            https://code.citrite.net/projects/XS/repos/sm-core-libs
Source0: sm-core-libs-0.13.1.tar.gz
BuildArch:      noarch

## Pull in the correct RPM macros for the distributon
## (Any fedora which is still in support uses python3)
%if 0%{?centos} > 7 || 0%{?rhel} > 7 || 0%{?fedora} > 0
BuildRequires: python3-rpm-macros
BuildRequires:  python3-setuptools
BuildRequires: python-nose
BuildRequires: python3-coverage
%global py_sitelib %{python3_sitelib}
%global __python %{__python3}
%else
BuildRequires: python2-rpm-macros
BuildRequires:  python2-setuptools
BuildRequires: python-nose
BuildRequires: python-coverage
BuildRequires: python2-mock
%global py_sitelib %{python2_sitelib}
%global __python %{__python2}
%endif

%description
This package contains common core libraries for SM.


%prep
%autosetup -p1


%build
sed -i "s/\(version='\)[^'\"]\+/\1%{version}-%{release}/g" setup.py
%{__python} setup.py build

%install
sed -i "s/\(version='\)[^'\"]\+/\1%{version}-%{release}/g" setup.py
%{__python} setup.py install --single-version-externally-managed -O1 --root=$RPM_BUILD_ROOT


%check
tests/run_unit_tests.sh
cp .coverage %{buildroot}
cp coverage.xml %{buildroot}
cp -r htmlcov %{buildroot}/htmlcov

%files
%{py_sitelib}/sm/__init__.py*
%{py_sitelib}/sm/core
%{py_sitelib}/sm_core_libs-*.egg-info

%package testresults
Group:    System/Hypervisor
Summary:  test results for SM core libs package

%description testresults
The package contains the build time test results for the SM core libs package

%files testresults
/.coverage
/coverage.xml
/htmlcov

%changelog
* Fri Feb 11 2022 Mark Syms <mark.syms@citrix.com> - 0.13.1-1
- CA-363533: rescan when requested and refcounts are > 1

* Fri Nov 05 2021 Mark Syms <mark.syms@citrix.com> - 0.13.0-2
- Rebuild

* Thu May 06 2021 Mark Syms <mark.syms@citrix.com> - 0.13.0-1
- add get_iscsi_interfaces to libiscsi
- Enable SonarQube
- Run unit tests and fix build dependencies

* Fri Jun 14 2019 Mark Syms <mark.syms@citrix.com> - 0.12.1-2
- Use longer timeouts on connectivity check

* Thu Nov  1 2018 Mark Syms <mark.syms@citrix.com> - 0.12.0-2
- Update requirements for LVM2 version

* Tue Jul 31 2018 Robert Breker <robert.breker@citrix.com> - 0.11.0-1
- CA-294559: Initial package
