Name:           arequal
Version:        1.1
Release:        3%{?dist}
Summary:        Tool to test data integrity of GlusterFS

License:        GPLv3+
URL:            https://github.com/nigelbabu/arequal
Source0:        https://github.com/nigelbabu/arequal/archive/%{version}.tar.gz

%description
This is a tool to test the data integrity of GlusterFS. It's used in the tests.

%prep
%autosetup


%build
./autogen.sh
%configure
%make_build


%install
rm -rf $RPM_BUILD_ROOT
%make_install


%files
%license LICENSE
%doc README
/usr/bin/arequal-checksum
%exclude /usr/bin/arequal-run.sh



%changelog
* Tue Dec 13 2016 Nigel Babu <nigelb@redhat.com> - 1.1-1
- Fix the license to GPLv3 and fix email address

* Tue Dec 13 2016 Nigel Babu <nigelb@redhat.com> - 1.0-1
- Initial RPM release.
