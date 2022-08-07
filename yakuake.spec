Summary:	Very powerful Quake style Konsole
Name:		yakuake
Version:	22.07.90
Release:	1
License:	GPLv2+
Group:		Graphical desktop/KDE
Url:		http://www.kde-apps.org/content/show.php?content=29153
Source0:	https://download.kde.org/%([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)/release-service/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(KF5Archive)
BuildRequires:	cmake(KF5Config)
BuildRequires:	cmake(KF5CoreAddons)
BuildRequires:	cmake(KF5Crash)
BuildRequires:	cmake(KF5DBusAddons)
BuildRequires:	cmake(KF5GlobalAccel)
BuildRequires:	cmake(KF5I18n)
BuildRequires:	cmake(KF5IconThemes)
BuildRequires:	cmake(KF5KIO)
BuildRequires:	cmake(KF5NewStuff)
BuildRequires:	cmake(KF5Notifications)
BuildRequires:	cmake(KF5NotifyConfig)
BuildRequires:	cmake(KF5Parts)
BuildRequires:	cmake(KF5WidgetsAddons)
BuildRequires:	cmake(KF5WindowSystem)
BuildRequires:	cmake(KF5Wayland)
BuildRequires:	pkgconfig(Qt5Core)
BuildRequires:	pkgconfig(Qt5Widgets)
BuildRequires:	pkgconfig(Qt5X11Extras)
BuildRequires:  pkgconfig(Qt5Svg)
Requires:	konsole
Obsoletes:	kde4-yakuake <= 2.9.2
Provides:	kde4-yakuake = 3.0.0

%description
Yakuake is a Quake-style terminal emulator based on KDE Konsole technology.

%files -f %{name}.lang
%doc AUTHORS ChangeLog README.md TODO NEWS
%dir %{_datadir}/%{name}
%{_bindir}/%{name}
%{_datadir}/metainfo/org.kde.yakuake.appdata.xml
%{_datadir}/applications/org.kde.yakuake.desktop
%{_iconsdir}/hicolor/*/apps/%{name}.png
%{_datadir}/knotifications5/%{name}.notifyrc
%{_datadir}/%{name}/skins
%{_datadir}/dbus-1/services/org.kde.yakuake.service
%{_datadir}/knsrcfiles/yakuake.knsrc

#--------------------------------------------------------------------

%prep
%setup -q
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build

%find_lang %name
