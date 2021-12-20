Name:           sm-core-libs
Version:        0.13.0
Release:        1%{?dist}
Summary:        sm core libraries - SM common core libraries.

License:        LGPL
URL:            https://code.citrite.net/projects/XS/repos/sm-core-libs

Source0: https://code.citrite.net/rest/archive/latest/projects/XS/repos/sm-core-libs/archive?at=v0.13.0&format=tar.gz&prefix=sm-core-libs-0.13.0#/sm-core-libs-0.13.0.tar.gz


Provides: gitsha(https://code.citrite.net/rest/archive/latest/projects/XS/repos/sm-core-libs/archive?at=v0.13.0&format=tar.gz&prefix=sm-core-libs-0.13.0#/sm-core-libs-0.13.0.tar.gz) = e872eca074fdb7f0e27ef7f29b3694f1cefdd656

BuildArch:      noarch

BuildRequires:  python-setuptools python-nose python-coverage python2-mock
Requires: 		xenserver-lvm2 >= 2.02.177

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
%{python_sitelib}/sm/__init__.py*
%{python_sitelib}/sm/core
%{python_sitelib}/sm_core_libs-*.egg-info

%package testresults
Provides: gitsha(https://code.citrite.net/rest/archive/latest/projects/XS/repos/sm-core-libs/archive?at=v0.13.0&format=tar.gz&prefix=sm-core-libs-0.13.0#/sm-core-libs-0.13.0.tar.gz) = e872eca074fdb7f0e27ef7f29b3694f1cefdd656
Group:    System/Hypervisor
Summary:  test results for SM core libs package

%description testresults
The package contains the build time test results for the SM core libs package

%files testresults
/.coverage
/coverage.xml
/htmlcov

%changelog
* Thu May 06 2021 Mark Syms <mark.syms@citrix.com> - 0.13.0-1
- add get_iscsi_interfaces to libiscsi

* Fri Jun 14 2019 Mark Syms <mark.syms@citrix.com> - 0.12.1-2
- Use longer timeouts on connectivity check

* Thu Nov  1 2018 Mark Syms <mark.syms@citrix.com> - 0.12.0-2
- Update requirements for LVM2 version

* Tue Jul 31 2018 Robert Breker <robert.breker@citrix.com> - 0.11.0-1
- CA-294559: Initial package
