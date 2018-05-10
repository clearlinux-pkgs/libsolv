#


#
Name     : libsolv
Version  : 0.6.31
Release  : 10
URL      : https://github.com/openSUSE/libsolv/archive/0.6.31.tar.gz
Source0  : https://github.com/openSUSE/libsolv/archive/0.6.31.tar.gz
Summary  : Library for solving packages
Group    : Development/Tools
License  : BSD-3-Clause
Requires: libsolv-bin
Requires: libsolv-lib
Requires: libsolv-data
Requires: libsolv-doc
BuildRequires : cmake
BuildRequires : db-dev
BuildRequires : pkgconfig(expat)
BuildRequires : pkgconfig(liblzma)
BuildRequires : pkgconfig(rpm)
BuildRequires : zlib-dev

%description
This is libsolv, a free package dependency solver using a satisfiability
algorithm.

%package bin
Summary: bin components for the libsolv package.
Group: Binaries
Requires: libsolv-data

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
Requires: libsolv-lib
Requires: libsolv-bin
Requires: libsolv-data
Provides: libsolv-devel

%description dev
dev components for the libsolv package.


%package doc
Summary: doc components for the libsolv package.
Group: Documentation

%description doc
doc components for the libsolv package.


%package lib
Summary: lib components for the libsolv package.
Group: Libraries
Requires: libsolv-data

%description lib
lib components for the libsolv package.


%prep
%setup -q -n libsolv-0.6.31

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1517494610
mkdir clr-build
pushd clr-build
cmake .. -G "Unix Makefiles" -DCMAKE_INSTALL_PREFIX=/usr -DBUILD_SHARED_LIBS:BOOL=ON -DLIB_INSTALL_DIR:PATH=/usr/lib64 -DCMAKE_AR=/usr/bin/gcc-ar -DLIB_SUFFIX=64 -DCMAKE_BUILD_TYPE=RelWithDebInfo -DCMAKE_RANLIB=/usr/bin/gcc-ranlib -DENABLE_COMPLEX_DEPS=YES -DENABLE_RPMDB=YES -DENABLE_RPMMD=YES -DENABLE_LZMA_COMPRESSION=yes
make VERBOSE=1  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1517494610
rm -rf %{buildroot}
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
/usr/bin/repo2solv.sh
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

%files doc
%defattr(-,root,root,-)
%doc /usr/share/man/man1/*
%doc /usr/share/man/man3/*

%files lib
%defattr(-,root,root,-)
/usr/lib64/libsolv.so.0
/usr/lib64/libsolvext.so.0
