Name:           sm-core-libs
Version:        0.12.0
Release:        2%{?dist}
Summary:        sm core libraries - SM common core libraries.

License:        LGPL
URL:            https://code.citrite.net/projects/XS/repos/sm-core-libs

Source0: https://code.citrite.net/rest/archive/latest/projects/XS/repos/sm-core-libs/archive?at=v0.12.0&format=tar.gz&prefix=sm-core-libs-0.12.0#/sm-core-libs-0.12.0.tar.gz


Provides: gitsha(https://code.citrite.net/rest/archive/latest/projects/XS/repos/sm-core-libs/archive?at=v0.12.0&format=tar.gz&prefix=sm-core-libs-0.12.0#/sm-core-libs-0.12.0.tar.gz) = c7218ae7a8bbe752e71daebd82838ef64ffc3ecb

BuildArch:      noarch

BuildRequires:  python-devel python-setuptools
Requires: 		xenserver-lvm2 >= 2.02.177

%description
This package contains common core libraries for SM.


%prep
%autosetup -p1


%install
./setup.py install --single-version-externally-managed -O1 --root=$RPM_BUILD_ROOT


%files
%{python_sitelib}/sm/__init__.py*
%{python_sitelib}/sm/core
%{python_sitelib}/sm_core_libs-*.egg-info


%changelog
* Thu Nov  1 2018 Mark Syms <mark.syms@citrix.com> - 0.12.0-2
- Update requirements for LVM2 version

* Tue Jul 31 2018 Robert Breker <robert.breker@citrix.com> - 0.11.0-1
- CA-294559: Initial package
