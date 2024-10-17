%define major 0
%define libname %mklibname %{name} %{major}
%define devname %mklibname -d %{name}

Summary:	Apple Lossless Audio Codec (ALAC)
Name:		alac
Version:	0.2.0
Release:	1
Group:		Sound
License:	Apple Public Source License
Url:		https://alac.macosforge.org/
Source0:	https://github.com/macosforge/alac/archive/master/alac-20210101.tar.gz
Patch0:		alac-0.1-makefile.patch

%description
The Apple Lossless Audio Codec (ALAC) is an audio codec developed by Apple and
supported on iPhone, iPad, most iPods, Mac and iTunes.  ALAC is a data
compression method which reduces the size of audio files with no loss
of information.  A decoded ALAC stream is bit-for-bit identical to the original
uncompressed audio file.

%package -n %{libname}
Summary:	Apple Lossless Audio Codec
Group:		System/Libraries
Obsoletes:	%{_lib}name < 0.1-1.20111026.2

%description -n %{libname}
The Apple Lossless Audio Codec (ALAC) is an audio codec developed by Apple and
supported on iPhone, iPad, most iPods, Mac and iTunes.  ALAC is a data
compression method which reduces the size of audio files with no loss
of information.  A decoded ALAC stream is bit-for-bit identical to the original
uncompressed audio file.

%package -n %{devname}
Summary:	Apple Lossless Audio Codec
Group:		Development/C++
Requires:	%{libname} = %{version}-%{release}
Obsoletes:	%{_lib}alac-static-devel < 0.1-1.20111026.2

%description -n %{devname}
The Apple Lossless Audio Codec (ALAC) is an audio codec developed by Apple and
supported on iPhone, iPad, most iPods, Mac and iTunes.  ALAC is a data
compression method which reduces the size of audio files with no loss
of information.  A decoded ALAC stream is bit-for-bit identical to the original
uncompressed audio file.

%package -n alacconvert
Summary:	Apple Lossless Audio Codec
Group:		Sound

%description -n alacconvert
The Apple Lossless Audio Codec (ALAC) is an audio codec developed by Apple and
supported on iPhone, iPad, most iPods, Mac and iTunes.  ALAC is a data
compression method which reduces the size of audio files with no loss of
information.  A decoded ALAC stream is bit-for-bit identical to the original
uncompressed audio file.

This package contains a command-line utility to convert the ALAC format.

%prep
%autosetup -p0 -n alac-master

%build
for d in codec convert-utility; do
    make -C "$d" \
        OPTFLAGS="%{optflags}" \
        CC="%__cxx"
done

%install
install -D -m0755 convert-utility/alacconvert %{buildroot}%{_bindir}/alacconvert

install -d %{buildroot}%{_includedir}
cp -a codec/*.h %{buildroot}%{_includedir}/

install -d %{buildroot}%{_libdir}
cp -a codec/libalac.so* %{buildroot}%{_libdir}/

%files -n %{libname}
%doc codec/APPLE_LICENSE.txt
%{_libdir}/libalac.so.%{major}*

%files -n %{devname}
%{_includedir}/*.h
%{_libdir}/libalac.so

%files -n alacconvert
%doc ReadMe.txt ALACMagicCookieDescription.txt LICENSE
%{_bindir}/alacconvert

