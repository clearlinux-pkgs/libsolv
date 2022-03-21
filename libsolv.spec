#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : libsolv
Version  : 0.7.22
Release  : 31
URL      : https://github.com/openSUSE/libsolv/archive/0.7.22/libsolv-0.7.22.tar.gz
Source0  : https://github.com/openSUSE/libsolv/archive/0.7.22/libsolv-0.7.22.tar.gz
Summary  : Library for solving packages
Group    : Development/Tools
License  : BSD-3-Clause MIT
Requires: libsolv-bin = %{version}-%{release}
Requires: libsolv-data = %{version}-%{release}
Requires: libsolv-lib = %{version}-%{release}
Requires: libsolv-license = %{version}-%{release}
Requires: libsolv-man = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : pkg-config
BuildRequires : pkgconfig(expat)
BuildRequires : pkgconfig(liblzma)
BuildRequires : pkgconfig(rpm)
BuildRequires : zlib-dev

%description
Libsolv
=======
This is libsolv, a free package dependency solver using a satisfiability
algorithm.

%package bin
Summary: bin components for the libsolv package.
Group: Binaries
Requires: libsolv-data = %{version}-%{release}
Requires: libsolv-license = %{version}-%{release}

%description bin
bin components for the libsolv package.


%package data
Summary: data components for the libsolv package.
Group: Data

%description data
data components for the libsolv package.


%package dev
Summary: dev components for the libsolv package.
Group: Development
Requires: libsolv-lib = %{version}-%{release}
Requires: libsolv-bin = %{version}-%{release}
Requires: libsolv-data = %{version}-%{release}
Provides: libsolv-devel = %{version}-%{release}
Requires: libsolv = %{version}-%{release}

%description dev
dev components for the libsolv package.


%package lib
Summary: lib components for the libsolv package.
Group: Libraries
Requires: libsolv-data = %{version}-%{release}
Requires: libsolv-license = %{version}-%{release}

%description lib
lib components for the libsolv package.


%package license
Summary: license components for the libsolv package.
Group: Default

%description license
license components for the libsolv package.


%package man
Summary: man components for the libsolv package.
Group: Default

%description man
man components for the libsolv package.


%prep
%setup -q -n libsolv-0.7.22
cd %{_builddir}/libsolv-0.7.22

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1647893989
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
%cmake .. -DENABLE_COMPLEX_DEPS=YES \
-DENABLE_RPMDB=YES \
-DENABLE_RPMDB_BYRPMHEADER=YES \
-DENABLE_RPMDB_LIBRPM=YES \
-DENABLE_RPMPKG_LIBRPM=YES \
-DENABLE_RPMMD=YES \
-DENABLE_LZMA_COMPRESSION=yes \
-DENABLE_ZCHUNK_COMPRESSION=OFF
make  %{?_smp_mflags}
popd

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make -C clr-build test %{?_smp_mflags:ARGS=%{_smp_mflags}}

%install
export SOURCE_DATE_EPOCH=1647893989
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/libsolv
cp %{_builddir}/libsolv-0.7.22/LICENSE.BSD %{buildroot}/usr/share/package-licenses/libsolv/b965854f0ddcbff41631dee1f018ba72e2f248ff
cp %{_builddir}/libsolv-0.7.22/win32/LICENSE %{buildroot}/usr/share/package-licenses/libsolv/bf81e90c601de42748bc87dfbee410eabd40cf90
pushd clr-build
%make_install
popd

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/deltainfoxml2solv
/usr/bin/dumpsolv
/usr/bin/installcheck
/usr/bin/mergesolv
/usr/bin/repo2solv
/usr/bin/repomdxml2solv
/usr/bin/rpmdb2solv
/usr/bin/rpmmd2solv
/usr/bin/rpms2solv
/usr/bin/testsolv
/usr/bin/updateinfoxml2solv

%files data
%defattr(-,root,root,-)
/usr/share/cmake/*

%files dev
%defattr(-,root,root,-)
/usr/include/solv/bitmap.h
/usr/include/solv/chksum.h
/usr/include/solv/dataiterator.h
/usr/include/solv/dirpool.h
/usr/include/solv/evr.h
/usr/include/solv/hash.h
/usr/include/solv/knownid.h
/usr/include/solv/policy.h
/usr/include/solv/pool.h
/usr/include/solv/pool_fileconflicts.h
/usr/include/solv/pool_parserpmrichdep.h
/usr/include/solv/poolarch.h
/usr/include/solv/poolid.h
/usr/include/solv/pooltypes.h
/usr/include/solv/poolvendor.h
/usr/include/solv/problems.h
/usr/include/solv/queue.h
/usr/include/solv/repo.h
/usr/include/solv/repo_deltainfoxml.h
/usr/include/solv/repo_repomdxml.h
/usr/include/solv/repo_rpmdb.h
/usr/include/solv/repo_rpmmd.h
/usr/include/solv/repo_solv.h
/usr/include/solv/repo_updateinfoxml.h
/usr/include/solv/repo_write.h
/usr/include/solv/repodata.h
/usr/include/solv/rules.h
/usr/include/solv/selection.h
/usr/include/solv/solv_xfopen.h
/usr/include/solv/solvable.h
/usr/include/solv/solver.h
/usr/include/solv/solverdebug.h
/usr/include/solv/solvversion.h
/usr/include/solv/strpool.h
/usr/include/solv/testcase.h
/usr/include/solv/tools_util.h
/usr/include/solv/transaction.h
/usr/include/solv/util.h
/usr/lib64/libsolv.so
/usr/lib64/libsolvext.so
/usr/lib64/pkgconfig/libsolv.pc
/usr/lib64/pkgconfig/libsolvext.pc
/usr/share/man/man3/libsolv-bindings.3
/usr/share/man/man3/libsolv-constantids.3
/usr/share/man/man3/libsolv-history.3
/usr/share/man/man3/libsolv-pool.3
/usr/share/man/man3/libsolv.3

%files lib
%defattr(-,root,root,-)
/usr/lib64/libsolv.so.1
/usr/lib64/libsolvext.so.1

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/libsolv/b965854f0ddcbff41631dee1f018ba72e2f248ff
/usr/share/package-licenses/libsolv/bf81e90c601de42748bc87dfbee410eabd40cf90

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/deltainfoxml2solv.1
/usr/share/man/man1/dumpsolv.1
/usr/share/man/man1/installcheck.1
/usr/share/man/man1/mergesolv.1
/usr/share/man/man1/repo2solv.1
/usr/share/man/man1/repomdxml2solv.1
/usr/share/man/man1/rpmdb2solv.1
/usr/share/man/man1/rpmmd2solv.1
/usr/share/man/man1/rpms2solv.1
/usr/share/man/man1/solv.1
/usr/share/man/man1/testsolv.1
/usr/share/man/man1/updateinfoxml2solv.1
