#define git 20240218
%define gitbranch release/24.02
%define gitbranchd %(echo %{gitbranch} |sed -e "s,/,-,g")
Summary:	Very powerful Quake style Konsole
Name:		plasma6-yakuake
Version:	24.02.1
Release:	%{?git:0.%{git}.}1
License:	GPLv2+
Group:		Graphical desktop/KDE
Url:		http://www.kde-apps.org/content/show.php?content=29163
%if 0%{?git:1}
Source0:	https://invent.kde.org/utilities/yakuake/-/archive/%{gitbranch}/yakuake-%{gitbranchd}.tar.bz2#/yakuake-%{git}.tar.bz2
%else
Source0:	https://download.kde.org/%([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)/release-service/%{version}/src/yakuake-%{version}.tar.xz
%endif
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(KF6Archive)
BuildRequires:	cmake(KF6Config)
BuildRequires:	cmake(KF6CoreAddons)
BuildRequires:	cmake(KF6Crash)
BuildRequires:	cmake(KF6DBusAddons)
BuildRequires:	cmake(KF6GlobalAccel)
BuildRequires:	cmake(KF6I18n)
BuildRequires:	cmake(KF6IconThemes)
BuildRequires:	cmake(KF6KIO)
BuildRequires:	cmake(KF6NewStuff)
BuildRequires:	cmake(KF6Notifications)
BuildRequires:	cmake(KF6NotifyConfig)
BuildRequires:	cmake(KF6Parts)
BuildRequires:	cmake(KF6WidgetsAddons)
BuildRequires:	cmake(KF6WindowSystem)
BuildRequires:	cmake(KF6StatusNotifierItem)
BuildRequires:	pkgconfig(Qt6Core)
BuildRequires:	pkgconfig(Qt6Widgets)
BuildRequires:  pkgconfig(Qt6Svg)
Requires:	plasma6-konsole

%description
Yakuake is a Quake-style terminal emulator based on KDE Konsole technology.

%files -f yakuake.lang
%doc AUTHORS ChangeLog README.md TODO NEWS
%dir %{_datadir}/yakuake
%{_bindir}/yakuake
%{_datadir}/metainfo/org.kde.yakuake.appdata.xml
%{_datadir}/applications/org.kde.yakuake.desktop
%{_iconsdir}/hicolor/*/apps/yakuake.png
%{_datadir}/knotifications6/yakuake.notifyrc
%{_datadir}/yakuake/skins
%{_datadir}/dbus-1/services/org.kde.yakuake.service
%{_datadir}/knsrcfiles/yakuake.knsrc

#--------------------------------------------------------------------

%prep
%autosetup -p1 -n yakuake-%{?git:%{gitbranchd}}%{!?git:%{version}}
%cmake \
	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON \
	-G Ninja

%build
%ninja -C build

%install
%ninja_install -C build

%find_lang yakuake
