#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : xorriso
Version  : 1.4.6
Release  : 11
URL      : http://ftp.gnu.org/gnu/xorriso/xorriso-1.4.6.tar.gz
Source0  : http://ftp.gnu.org/gnu/xorriso/xorriso-1.4.6.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0 GPL-3.0 LGPL-2.1
Requires: xorriso-bin
Requires: xorriso-doc
BuildRequires : acl-dev
BuildRequires : attr-dev
BuildRequires : bzip2-dev

%description
------------------------------------------------------------------------------
Contribution of libburnia-project.org to the GNU Operating System
------------------------------------------------------------------------------
GNU xorriso. By Thomas Schmitt <scdbackup@gmx.net>
Derived from and supported by libburnia-project.org, published via:
http://www.gnu.org/software/xorriso/xorriso_eng.html
http://www.gnu.org/software/xorriso/xorriso-1.4.6.tar.gz
Provided under GPL version 3 or later. No warranty.
------------------------------------------------------------------------------

%package bin
Summary: bin components for the xorriso package.
Group: Binaries

%description bin
bin components for the xorriso package.


%package doc
Summary: doc components for the xorriso package.
Group: Documentation

%description doc
doc components for the xorriso package.


%prep
%setup -q -n xorriso-1.4.6

%build
export LANG=C
%configure --disable-static
make V=1  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
%exclude /usr/bin/xorriso-tcltk
/usr/bin/osirrox
/usr/bin/xorrecord
/usr/bin/xorriso
/usr/bin/xorrisofs

%files doc
%defattr(-,root,root,-)
%doc /usr/share/info/*
%doc /usr/share/man/man1/*
