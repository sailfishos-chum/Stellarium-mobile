Name:       stellarium
Summary:    Planetary application
Version:    1.29.6
Release:    1
Group:      Qt/Qt
License:    GPLv2
URL:        https://github.com/sailfishos-chum/Stellarium-sailfishos
Source0:    %{name}-%{version}.tar.bz2
Source1:    stellarium-rpmlintrc
Requires:   sailfishsilica-qt5 >= 0.10.9
Requires:   qt5-qtdeclarative-import-localstorageplugin
Requires:   qt5-qtdeclarative-import-particles2
Requires:   qt5-qtpositioning
Requires:   qt5-qtsensors
BuildRequires:  pkgconfig(sailfishapp) >= 1.0.2
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Qml)
BuildRequires:  pkgconfig(Qt5Quick)
BuildRequires:  pkgconfig(Qt5Positioning)
BuildRequires:  pkgconfig(Qt5Sensors)
BuildRequires:  qt5-qttools-linguist
BuildRequires:  desktop-file-utils

%description
Stellarium for Sailfish adapted from Stellarium Mobile source.

Stellarium renders 3D photo-realistic skies in real time with OpenGL. It displays stars, constellations, planets and nebulae, and has many other features including multiple panoramic landscapes, fog and light pollution simulation.

Stellarium comes with a star catalogue of about 600 thousand stars and it is possible to download extra catalogues with up to 210 million stars.

Stellarium has multiple sky cultures - see the constellations from the traditions of Polynesian, Inuit, Navajo, Korean, Lakota, Egyptian and Chinese astronomers, as well as the traditional Western constellations.

# This description section includes metadata for SailfishOS:Chum, see
# https://github.com/sailfishos-chum/main/blob/main/Metadata.md
%if "%{?vendor}" == "chum"
PackageName: Stellarium
Type: desktop-application
DeveloperName: fuchsmich, lduboeuf, chengxinlun
PackagerName: DrYak
Categories:
  - Science
Custom:
  Repo: https://github.com/sailfishos-chum/Stellarium-sailfishos
Icon: https://github.com/sailfishos-chum/Stellarium-sailfishos/raw/master/icons/256x256/stellarium.png
Screenshots:
  - https://sailfishos-chum.github.io/Stellarium-sailfishos/screenshots/Screenshot_20220801_001.png
Url:
  Homepage: https://github.com/sailfishos-chum/Stellarium-sailfishos
  Bugtracker: https://github.com/sailfishos-chum/Stellarium-sailfishos/issues
%endif


%prep
%setup -q -n %{name}-%{version}


%build

%qmake5 

make %{?_smp_mflags}


%install
rm -rf %{buildroot}
%qmake5_install

desktop-file-install --delete-original       \
  --dir %{buildroot}%{_datadir}/applications             \
   %{buildroot}%{_datadir}/applications/*.desktop

%files
%defattr(-,root,root,-)
%{_bindir}/*
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png
