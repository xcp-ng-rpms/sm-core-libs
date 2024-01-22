%global package_speccommit 5ffb6a88fbcd9a6ac9e5faad548be3eb65820b2c
%global package_srccommit v1.0.2

%global srcname sm-core-libs
%global sum sm core libraries - SM common core libraries.
%global pkgdesc \
This package contains common core libraries for SM.

Name:    %{srcname}
Version: 1.0.2
Release: 1%{?xsrel}%{?dist}
Summary: %{sum}

License:        LGPL
URL:            https://code.citrite.net/projects/XS/repos/sm-core-libs
Source0: sm-core-libs-1.0.2.tar.gz
BuildArch:      noarch

%if 0%{?centos} > 7 || 0%{?rhel} > 7 || 0%{?fedora} > 0
BuildRequires:  python36-future
%else
BuildRequires:  python2-future
%endif

%description %{pkgdesc}


%package -n python2-%{srcname}
Summary:        %{sum}
Provides:       python-%{srcname} = %{version}-%{release}
Provides:       %{srcname}
Obsoletes:      %{srcname} < 1.0.0
Requires:        python2-future

BuildRequires: python2-rpm-macros
BuildRequires: python2-setuptools
BuildRequires: python-nose
BuildRequires: python-coverage
BuildRequires: python2-mock

%description -n python2-%{srcname} %{pkgdesc}

%package -n python%{python3_pkgversion}-%{srcname}
Summary:        %{sum}
Provides:       python%{python3_pkgversion}-%{srcname} = %{version}-%{release}
Requires:       python36-future

BuildRequires: python3-rpm-macros
BuildRequires: python3-setuptools

%description -n python%{python3_pkgversion}-%{srcname} %{pkgdesc}

%prep
%autosetup -p1


%build
sed -i "s/\(version='\)[^'\"]\+/\1%{version}-%{release}/g" setup.py
%py2_build
%py3_build

%install
sed -i "s/\(version='\)[^'\"]\+/\1%{version}-%{release}/g" setup.py
%py2_install
%py3_install

%check
tests/run_unit_tests.sh
cp .coverage %{buildroot}
cp coverage.xml %{buildroot}
cp -r htmlcov %{buildroot}/htmlcov

%files -n python2-%{srcname}
%{python2_sitelib}/*

%files -n python%{python3_pkgversion}-%{srcname}
%{python3_sitelib}/*

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
* Thu Oct 05 2023 Tim Smith <tim.smith@citrix.com> - 1.0.2-1
- CP-40123 Fix encodings for python3
- CP-40107: refcount files need to seek to 0 before reading

* Thu Jul 07 2022 Mark Syms <mark.syms@citrix.com> - 1.0.1-1
- CP-40107: Build python2 and python3 RPMs

* Thu Jun 30 2022  <mark.syms@citrix.com> - 1.0.0-1%{?dist}
- Make Python3 compatible rpm

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
