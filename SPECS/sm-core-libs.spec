Name:           sm-core-libs
Version:        0.11.0
Release:        1%{?dist}
Summary:        sm core libraries - SM common core libraries.

License:        LGPL
URL:            https://code.citrite.net/projects/XS/repos/sm-core-libs
Source0:        https://code.citrite.net/rest/archive/latest/projects/XS/repos/sm-core-libs/archive?at=v%{version}&format=tar.gz&prefix=%{name}-%{version}#/%{name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python-devel python-setuptools

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
* Tue Jul 31 2018 Robert Breker <robert.breker@citrix.com> - 0.11.0-1
- CA-294559: Initial package
