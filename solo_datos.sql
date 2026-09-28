--
-- PostgreSQL database dump
--

\restrict DVsZ90eTEcqdCV3c2a8kL8rpbtynm2KQhFDSSi43Rw6ytMUNwauv0yytNKZSOxU

-- Dumped from database version 18.4
-- Dumped by pg_dump version 18.4

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET transaction_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Data for Name: roles; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.roles (id, nombre) FROM stdin;
1	inspector
\.


--
-- Data for Name: usuarios; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.usuarios (id, username, hashed_password, activo, rol_id) FROM stdin;
fa095a27-4e47-4099-b6a4-f4bd34650fbc	11111111-1	$2b$12$A4TYh1prrr4ircwNJP7Es.FuH6PYVC8Vgb5VEPhKIgeRhecSbfl/.	t	1
\.


--
-- Data for Name: auditoria_eventos; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.auditoria_eventos (id, entidad_id, entidad_tipo, accion, usuario_id, payload, fecha) FROM stdin;
e43ce8b5-40a2-4a23-a430-761307b06771	85a2f307-31b0-456b-ad4b-c3610d33cec4	InfraccionVehicular	CREACION_POR_SYNC	fa095a27-4e47-4099-b6a4-f4bd34650fbc	{"id": "85a2f307-31b0-456b-ad4b-c3610d33cec4", "ppu": "AAAA-13", "fecha": "2026-06-04T12:32:24", "fotos": ["7354e16a26f30fa3644ca171936ce6a62b99df4c476187c249c490ce729259df"], "status": "guardadoLocal", "coordenadas": "-35.9663609,-72.3114476", "descripcion": "bkgg", "firmaRechazo": true, "rutInfractor": "20281553-7", "tipoVehiculo": "Camioneta", "colorVehiculo": "Negro", "marcaVehiculo": "Hyundai", "nombreCompleto": "juan", "tipoInfraccionId": 2}	2026-06-04 12:44:38.375041-04
f9b24be3-c067-45b1-8ad6-f73445bacd07	fa095a27-4e47-4099-b6a4-f4bd34650fbc	UsuarioMfa	MFA_SETUP_INICIADO	fa095a27-4e47-4099-b6a4-f4bd34650fbc	{"message": "Inició configuración de MFA"}	2026-06-04 14:47:35.677817-04
dc7c4501-ced9-41cc-9377-06d72d15d201	fa095a27-4e47-4099-b6a4-f4bd34650fbc	UsuarioMfa	MFA_SETUP_INICIADO	fa095a27-4e47-4099-b6a4-f4bd34650fbc	{"message": "Inició configuración de MFA"}	2026-06-04 14:53:54.746856-04
be708508-71b1-42a6-a285-46871c3ae896	fa095a27-4e47-4099-b6a4-f4bd34650fbc	UsuarioMfa	MFA_SETUP_INICIADO	fa095a27-4e47-4099-b6a4-f4bd34650fbc	{"message": "Inició configuración de MFA"}	2026-06-04 14:54:48.869118-04
44efc380-3a75-4598-92d6-0fd64bac2853	fa095a27-4e47-4099-b6a4-f4bd34650fbc	UsuarioMfa	MFA_SETUP_INICIADO	fa095a27-4e47-4099-b6a4-f4bd34650fbc	{"message": "Inició configuración de MFA"}	2026-06-04 15:18:08.665472-04
90d092a3-70a8-4bc3-adbe-248134684c5e	fa095a27-4e47-4099-b6a4-f4bd34650fbc	UsuarioMfa	MFA_SETUP_INICIADO	fa095a27-4e47-4099-b6a4-f4bd34650fbc	{"message": "Inició configuración de MFA"}	2026-06-04 15:18:47.966003-04
6151a0aa-6a27-4c56-8a15-dfa302290c59	fa095a27-4e47-4099-b6a4-f4bd34650fbc	UsuarioMfa	MFA_ACTIVADO	fa095a27-4e47-4099-b6a4-f4bd34650fbc	{"message": "MFA confirmado y activado exitosamente"}	2026-06-04 15:18:51.035489-04
e83fe52b-250f-466e-95fa-7b0db521a9a3	fa095a27-4e47-4099-b6a4-f4bd34650fbc	UsuarioMfa	MFA_SETUP_INICIADO	fa095a27-4e47-4099-b6a4-f4bd34650fbc	{"message": "IniciÃ³ configuraciÃ³n de MFA"}	2026-06-04 15:32:50.666258-04
e16135af-d361-43d7-a8ad-e7ef9977870d	fa095a27-4e47-4099-b6a4-f4bd34650fbc	UsuarioMfa	MFA_SETUP_INICIADO	fa095a27-4e47-4099-b6a4-f4bd34650fbc	{"message": "IniciÃ³ configuraciÃ³n de MFA"}	2026-06-04 15:33:50.845034-04
933938ce-33e6-43d4-9727-3887eadc94bc	fa095a27-4e47-4099-b6a4-f4bd34650fbc	UsuarioMfa	MFA_ACTIVADO	fa095a27-4e47-4099-b6a4-f4bd34650fbc	{"message": "MFA confirmado y activado exitosamente"}	2026-06-04 15:33:53.974057-04
8f532563-c906-45ca-a5cb-5988fe88ad6f	fa095a27-4e47-4099-b6a4-f4bd34650fbc	UsuarioMfa	MFA_SETUP_INICIADO	fa095a27-4e47-4099-b6a4-f4bd34650fbc	{"message": "IniciÃ³ configuraciÃ³n de MFA"}	2026-06-04 16:05:56.883822-04
94d65e84-743a-403a-ae24-56e13890e486	fa095a27-4e47-4099-b6a4-f4bd34650fbc	UsuarioMfa	MFA_SETUP_INICIADO	fa095a27-4e47-4099-b6a4-f4bd34650fbc	{"message": "IniciÃ³ configuraciÃ³n de MFA"}	2026-06-04 16:06:34.989266-04
7bdf07d6-05d9-4eab-9bc1-d3bab2e36800	fa095a27-4e47-4099-b6a4-f4bd34650fbc	UsuarioMfa	MFA_ACTIVADO	fa095a27-4e47-4099-b6a4-f4bd34650fbc	{"message": "MFA confirmado y activado exitosamente"}	2026-06-04 16:06:37.587321-04
e483d037-8a4c-4930-a04c-874fc5dca9e4	fa095a27-4e47-4099-b6a4-f4bd34650fbc	UsuarioMfa	MFA_SETUP_INICIADO	fa095a27-4e47-4099-b6a4-f4bd34650fbc	{"message": "IniciÃ³ configuraciÃ³n de MFA"}	2026-06-04 16:28:46.611102-04
e2bcd6b9-badc-4ffb-b30f-d7be586e31df	fa095a27-4e47-4099-b6a4-f4bd34650fbc	UsuarioMfa	MFA_SETUP_INICIADO	fa095a27-4e47-4099-b6a4-f4bd34650fbc	{"message": "IniciÃ³ configuraciÃ³n de MFA"}	2026-06-04 16:29:27.646699-04
4bd091c2-f808-4fd1-bbbd-a6d9b61100e4	fa095a27-4e47-4099-b6a4-f4bd34650fbc	UsuarioMfa	MFA_ACTIVADO	fa095a27-4e47-4099-b6a4-f4bd34650fbc	{"message": "MFA confirmado y activado exitosamente"}	2026-06-04 16:29:30.510097-04
4eba5005-edf2-4a5e-b1e7-e52a84b95140	fa095a27-4e47-4099-b6a4-f4bd34650fbc	UsuarioMfa	MFA_REVOCADO	fa095a27-4e47-4099-b6a4-f4bd34650fbc	{"message": "MFA revocado por el usuario"}	2026-06-04 16:30:20.449563-04
c304a659-754c-425c-a9a5-9bdb1fd13c70	fa095a27-4e47-4099-b6a4-f4bd34650fbc	UsuarioMfa	MFA_SETUP_INICIADO	fa095a27-4e47-4099-b6a4-f4bd34650fbc	{"message": "IniciÃ³ configuraciÃ³n de MFA"}	2026-06-04 16:30:49.530341-04
ae22debf-3220-48b2-9f0e-dd66dc4611c8	fa095a27-4e47-4099-b6a4-f4bd34650fbc	UsuarioMfa	MFA_SETUP_INICIADO	fa095a27-4e47-4099-b6a4-f4bd34650fbc	{"message": "IniciÃ³ configuraciÃ³n de MFA"}	2026-06-04 16:31:20.54711-04
0c292b6c-9837-41a4-ae5d-ae00342fad9c	fa095a27-4e47-4099-b6a4-f4bd34650fbc	UsuarioMfa	MFA_ACTIVADO	fa095a27-4e47-4099-b6a4-f4bd34650fbc	{"message": "MFA confirmado y activado exitosamente"}	2026-06-04 16:31:23.303086-04
6a9ba36c-1029-40fa-a5d1-ba90df645dfe	80fa86ea-ea46-4cf8-a02a-07245c44e860	InfraccionVehicular	CREACION_POR_SYNC	fa095a27-4e47-4099-b6a4-f4bd34650fbc	{"id": "80fa86ea-ea46-4cf8-a02a-07245c44e860", "ppu": "AAAA-14", "fecha": "2026-06-04T17:32:01", "fotos": ["f67c74aade895042826ab836d52a6f0f089e9f882618377bee212cb8d08c12d7"], "status": "guardadoLocal", "coordenadas": "-35.966414,-72.3114332", "descripcion": "car", "firmaRechazo": true, "rutInfractor": "19354678-1", "tipoVehiculo": "Camioneta", "colorVehiculo": "Rojo", "marcaVehiculo": "Toyota", "nombreCompleto": "Alfonso ", "tipoInfraccionId": 2}	2026-06-04 17:32:06.079968-04
c5fadbcf-3eb6-4f96-9d32-fcb8e72a95c1	aa8236e9-59cf-4cc2-b4b2-7d19d1e6ba55	InfraccionVehicular	CREACION_POR_SYNC	fa095a27-4e47-4099-b6a4-f4bd34650fbc	{"id": "aa8236e9-59cf-4cc2-b4b2-7d19d1e6ba55", "ppu": "RCCU-67", "fecha": "2026-06-04T17:33:39", "fotos": ["03f5e458475a4b3a20255fad539f4cd56999fd66562bf37fd4cacf8ba17a35e6"], "status": "guardadoLocal", "coordenadas": "-35.9665495,-72.3112924", "descripcion": "ov", "firmaRechazo": false, "rutInfractor": "20192739-0", "tipoVehiculo": "volador", "colorVehiculo": "desconocido ", "marcaVehiculo": "desconocido ", "nombreCompleto": "aa", "tipoInfraccionId": 1}	2026-06-04 17:33:50.329435-04
4099ac81-6837-4494-a491-966c50397bb2	fa095a27-4e47-4099-b6a4-f4bd34650fbc	UsuarioMfa	MFA_REVOCADO	fa095a27-4e47-4099-b6a4-f4bd34650fbc	{"message": "MFA revocado por el usuario"}	2026-06-04 17:49:09.436436-04
9d68776a-293d-4a6e-ac63-8e74aeeda487	fa095a27-4e47-4099-b6a4-f4bd34650fbc	UsuarioMfa	MFA_SETUP_INICIADO	fa095a27-4e47-4099-b6a4-f4bd34650fbc	{"message": "IniciÃ³ configuraciÃ³n de MFA"}	2026-06-04 17:49:50.444669-04
517159fd-1e6a-4514-a564-9e0171484544	fa095a27-4e47-4099-b6a4-f4bd34650fbc	UsuarioMfa	MFA_ACTIVADO	fa095a27-4e47-4099-b6a4-f4bd34650fbc	{"message": "MFA confirmado y activado exitosamente"}	2026-06-04 17:50:18.034811-04
24083004-4442-4136-9c31-55e1c12b6537	25a62aca-329d-42d8-a051-a034d41fb8db	InfraccionVehicular	CREACION_POR_SYNC	fa095a27-4e47-4099-b6a4-f4bd34650fbc	{"id": "25a62aca-329d-42d8-a051-a034d41fb8db", "ppu": "HHHH-15", "fecha": "2026-06-05T13:44:20", "fotos": ["120f39f207910fec3cd964f80d4dbc477c0eb8023d53d11574a8a5612f62847a", "d839be22366426fe6edb3acc0fc04c82039a73fc85901af4803efc371ce960d1"], "status": "guardadoLocal", "coordenadas": "-35.9666397,-72.3112266", "descripcion": "hhh", "firmaRechazo": false, "rutInfractor": "20192739-0", "tipoVehiculo": "Automóvil", "colorVehiculo": "Rojo", "marcaVehiculo": "Hyundai", "nombreCompleto": "Pablo", "tipoInfraccionId": 2}	2026-06-05 14:05:21.422984-04
c127c828-5cfc-4bbc-990e-6390697a871b	1038f711-b944-40d8-891e-5e77ce8b1a8e	InfraccionVehicular	CREACION_POR_SYNC	fa095a27-4e47-4099-b6a4-f4bd34650fbc	{"id": "1038f711-b944-40d8-891e-5e77ce8b1a8e", "ppu": "AAAA-17", "fecha": "2026-06-05T14:35:18", "fotos": ["8543479c884d7b93ba26e2ecde2c461f05ffd37f63e99caf11ba5cb237ae0c3c"], "status": "guardadoLocal", "coordenadas": "-35.9665913,-72.3113221", "descripcion": "jhjgh", "firmaRechazo": false, "rutInfractor": "20192739-0", "tipoVehiculo": "Automóvil", "colorVehiculo": "Negro", "marcaVehiculo": "Chevrolet", "nombreCompleto": "Juanito", "tipoInfraccionId": 2}	2026-06-05 14:39:48.51185-04
44d3fa94-e21a-4843-b50e-6d192a707d25	b1373c24-da1a-4989-b7c2-c8504326d47e	InfraccionVehicular	CREACION_POR_SYNC	fa095a27-4e47-4099-b6a4-f4bd34650fbc	{"id": "b1373c24-da1a-4989-b7c2-c8504326d47e", "ppu": "AAAA-56", "fecha": "2026-06-05T14:40:34", "fotos": ["9c2dc08f8e1d921ab2b142ffcda89e3a0d09be8cf1dab4c34e881590ea503fb8"], "status": "guardadoLocal", "coordenadas": "-35.9666312,-72.3112316", "descripcion": "jjjj", "firmaRechazo": false, "rutInfractor": null, "tipoVehiculo": "Camioneta", "colorVehiculo": "Negro", "marcaVehiculo": "Hyundai", "nombreCompleto": "jghj", "tipoInfraccionId": 1}	2026-06-05 14:41:58.360684-04
d0a08a06-1b03-43b7-87d3-3a1cfaf7324f	2c4d888e-1198-4328-acb3-ae64d54c584d	InfraccionVehicular	CREACION_POR_SYNC	fa095a27-4e47-4099-b6a4-f4bd34650fbc	{"id": "2c4d888e-1198-4328-acb3-ae64d54c584d", "ppu": "AAAA-58", "fecha": "2026-06-05T14:40:59", "fotos": ["c7a7e4b29d8c531b7ef2e8b70df5c3342c7d725c0d5cec6d61db82cf9670abab"], "status": "guardadoLocal", "coordenadas": "-35.9665836,-72.3112799", "descripcion": "jjjj", "firmaRechazo": false, "rutInfractor": null, "tipoVehiculo": "Camioneta", "colorVehiculo": "Negro", "marcaVehiculo": "Hyundai", "nombreCompleto": "roberto", "tipoInfraccionId": 1}	2026-06-05 14:41:58.403635-04
03f2e2b6-3a58-4101-a23d-2c83c534cf01	8d5d3c56-65b5-4464-8787-630a21a54b72	InfraccionVehicular	CREACION_POR_SYNC	fa095a27-4e47-4099-b6a4-f4bd34650fbc	{"id": "8d5d3c56-65b5-4464-8787-630a21a54b72", "ppu": "AAAA-59", "fecha": "2026-06-05T14:41:33", "fotos": ["63e97784ff419a99d994f178af9613547c3b26d32603a95ce753c4eaa9cde235"], "status": "guardadoLocal", "coordenadas": "-35.9665373,-72.311356", "descripcion": "kkkkkk", "firmaRechazo": false, "rutInfractor": null, "tipoVehiculo": "Camioneta", "colorVehiculo": "Blanco", "marcaVehiculo": "Ford", "nombreCompleto": "Camilo", "tipoInfraccionId": 1}	2026-06-05 14:41:58.486279-04
d656b669-c9ba-4a84-b675-ad64d2db3bb3	dafc59ee-e8a3-43a0-b79e-07a441c20b6b	InfraccionVehicular	CREACION_POR_SYNC	fa095a27-4e47-4099-b6a4-f4bd34650fbc	{"id": "dafc59ee-e8a3-43a0-b79e-07a441c20b6b", "ppu": "S/P", "fecha": "2026-06-05T14:41:51", "fotos": ["d4973762136258fd77ea11a17974bf10f92b706208419ee3b94caf0be16b8558"], "status": "guardadoLocal", "coordenadas": "-35.9665248,-72.3116877", "descripcion": "kkkkkk", "firmaRechazo": false, "rutInfractor": null, "tipoVehiculo": "Camioneta", "colorVehiculo": "Blanco", "marcaVehiculo": "Ford", "nombreCompleto": "Camila", "tipoInfraccionId": 1}	2026-06-05 14:41:58.561209-04
\.


--
-- Data for Name: catalogo_infracciones; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.catalogo_infracciones (id, codigo_ley, descripcion, gravedad, costo_utm) FROM stdin;
1	ADV	Advertencia Empadronada	LEVE	0.00
2	JPL	Citacion JPL	GRAVE	1.50
\.


--
-- Data for Name: dispositivos_moviles; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.dispositivos_moviles (id, usuario_id, device_id, nombre_dispositivo, activo, revocado, last_seen_at, estado) FROM stdin;
a65e5397-a081-42cf-8dca-1defb4a6a31e	fa095a27-4e47-4099-b6a4-f4bd34650fbc	f0800999-4425-4e52-a292-eb2d32ffef53	\N	t	f	2026-06-05 19:05:54.905177	ACTIVO
\.


--
-- Data for Name: registros_base; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.registros_base (id, inspector_id, modulo, estado, fecha_emision, ubicacion, auditoria_jsonb) FROM stdin;
85a2f307-31b0-456b-ad4b-c3610d33cec4	fa095a27-4e47-4099-b6a4-f4bd34650fbc	infraccion_vehicular	guardadoLocal	2026-06-04 12:32:24-04	0101000020E6100000BB1AEAC1EE1352C00AD1C6B6B1FB41C0	\N
80fa86ea-ea46-4cf8-a02a-07245c44e860	fa095a27-4e47-4099-b6a4-f4bd34650fbc	infraccion_vehicular	guardadoLocal	2026-06-04 17:32:01-04	0101000020E6100000DF388485EE1352C0C2323674B3FB41C0	\N
aa8236e9-59cf-4cc2-b4b2-7d19d1e6ba55	fa095a27-4e47-4099-b6a4-f4bd34650fbc	infraccion_vehicular	guardadoLocal	2026-06-04 17:33:39-04	0101000020E6100000935FF536EC1352C08A3BDEE4B7FB41C0	\N
25a62aca-329d-42d8-a051-a034d41fb8db	fa095a27-4e47-4099-b6a4-f4bd34650fbc	infraccion_vehicular	guardadoLocal	2026-06-05 13:44:20-04	0101000020E61000004C29F922EB1352C0F44185D9BAFB41C0	\N
1038f711-b944-40d8-891e-5e77ce8b1a8e	fa095a27-4e47-4099-b6a4-f4bd34650fbc	infraccion_vehicular	guardadoLocal	2026-06-05 14:35:18-04	0101000020E6100000698187B3EC1352C08F0C8343B9FB41C0	\N
b1373c24-da1a-4989-b7c2-c8504326d47e	fa095a27-4e47-4099-b6a4-f4bd34650fbc	infraccion_vehicular	guardadoLocal	2026-06-05 14:40:34-04	0101000020E6100000D5DEF137EB1352C089A53792BAFB41C0	\N
2c4d888e-1198-4328-acb3-ae64d54c584d	fa095a27-4e47-4099-b6a4-f4bd34650fbc	infraccion_vehicular	guardadoLocal	2026-06-05 14:40:59-04	0101000020E6100000BD998702EC1352C0CB6CEB02B9FB41C0	\N
8d5d3c56-65b5-4464-8787-630a21a54b72	fa095a27-4e47-4099-b6a4-f4bd34650fbc	infraccion_vehicular	guardadoLocal	2026-06-05 14:41:33-04	0101000020E6100000755AB741ED1352C09CEE867EB7FB41C0	\N
dafc59ee-e8a3-43a0-b79e-07a441c20b6b	fa095a27-4e47-4099-b6a4-f4bd34650fbc	infraccion_vehicular	guardadoLocal	2026-06-05 14:41:51-04	0101000020E61000003084F7B0F21352C0F062AB15B7FB41C0	\N
\.


--
-- Data for Name: evidencias_fotograficas; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.evidencias_fotograficas (id, registro_uuid, hash_sha256) FROM stdin;
403e5827-bddb-4277-928a-b5189b9f1446	85a2f307-31b0-456b-ad4b-c3610d33cec4	7354e16a26f30fa3644ca171936ce6a62b99df4c476187c249c490ce729259df
351a9022-da7d-4937-9302-9434def6b052	80fa86ea-ea46-4cf8-a02a-07245c44e860	f67c74aade895042826ab836d52a6f0f089e9f882618377bee212cb8d08c12d7
02a981c7-8b5a-4681-9692-a5d8b903ed01	aa8236e9-59cf-4cc2-b4b2-7d19d1e6ba55	03f5e458475a4b3a20255fad539f4cd56999fd66562bf37fd4cacf8ba17a35e6
425f2f4b-d3f2-4e97-acec-dd7fd368368a	25a62aca-329d-42d8-a051-a034d41fb8db	120f39f207910fec3cd964f80d4dbc477c0eb8023d53d11574a8a5612f62847a
57f34472-5a9a-4baf-b899-cc57d198dbda	25a62aca-329d-42d8-a051-a034d41fb8db	d839be22366426fe6edb3acc0fc04c82039a73fc85901af4803efc371ce960d1
3ca6226b-9984-42d7-b74e-e0c43d763c5e	1038f711-b944-40d8-891e-5e77ce8b1a8e	8543479c884d7b93ba26e2ecde2c461f05ffd37f63e99caf11ba5cb237ae0c3c
d8fa769d-6b7d-4a61-9cf6-05f8b96333cb	b1373c24-da1a-4989-b7c2-c8504326d47e	9c2dc08f8e1d921ab2b142ffcda89e3a0d09be8cf1dab4c34e881590ea503fb8
5aec9f00-d56e-440e-a3b8-f16d38db6995	2c4d888e-1198-4328-acb3-ae64d54c584d	c7a7e4b29d8c531b7ef2e8b70df5c3342c7d725c0d5cec6d61db82cf9670abab
8812bb15-ad9b-438b-b24c-6a25622ca450	8d5d3c56-65b5-4464-8787-630a21a54b72	63e97784ff419a99d994f178af9613547c3b26d32603a95ce753c4eaa9cde235
2ee76311-fc7b-4f4a-8adb-16dddc4ca0b0	dafc59ee-e8a3-43a0-b79e-07a441c20b6b	d4973762136258fd77ea11a17974bf10f92b706208419ee3b94caf0be16b8558
\.


--
-- Data for Name: infracciones_vehiculares; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.infracciones_vehiculares (registro_uuid, ppu, marca, tipo_vehiculo, color, tipo_infraccion_id, observaciones, rut_infractor, nombre_completo) FROM stdin;
85a2f307-31b0-456b-ad4b-c3610d33cec4	AAAA-13	Hyundai	Camioneta	Negro	2	bkgg	20281553-7	juan
80fa86ea-ea46-4cf8-a02a-07245c44e860	AAAA-14	Toyota	Camioneta	Rojo	2	car	19354678-1	Alfonso 
aa8236e9-59cf-4cc2-b4b2-7d19d1e6ba55	RCCU-67	desconocido 	volador	desconocido 	1	ov	20192739-0	aa
25a62aca-329d-42d8-a051-a034d41fb8db	HHHH-15	Hyundai	Automóvil	Rojo	2	hhh	20192739-0	Pablo
1038f711-b944-40d8-891e-5e77ce8b1a8e	AAAA-17	Chevrolet	Automóvil	Negro	2	jhjgh	20192739-0	Juanito
b1373c24-da1a-4989-b7c2-c8504326d47e	AAAA-56	Hyundai	Camioneta	Negro	1	jjjj	\N	jghj
2c4d888e-1198-4328-acb3-ae64d54c584d	AAAA-58	Hyundai	Camioneta	Negro	1	jjjj	\N	roberto
8d5d3c56-65b5-4464-8787-630a21a54b72	AAAA-59	Ford	Camioneta	Blanco	1	kkkkkk	\N	Camilo
dafc59ee-e8a3-43a0-b79e-07a441c20b6b	S/P	Ford	Camioneta	Blanco	1	kkkkkk	\N	Camila
\.


--
-- Data for Name: sesiones_moviles; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.sesiones_moviles (id, usuario_id, dispositivo_id, token_hash, creada_at, expira_at, revocada) FROM stdin;
\.


--
-- Data for Name: spatial_ref_sys; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.spatial_ref_sys (srid, auth_name, auth_srid, srtext, proj4text) FROM stdin;
\.


--
-- Data for Name: sync_events; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.sync_events (id, dispositivo_id, inspector_id, fecha_sync, estado, detalles) FROM stdin;
9b048f6d-8707-4fe9-af19-349eacab6def	Fiscalis Mobile App	fa095a27-4e47-4099-b6a4-f4bd34650fbc	2026-06-04 12:44:38.377174-04	EXITOSO	{"modulo": "infraccion_vehicular", "acta_id": "85a2f307-31b0-456b-ad4b-c3610d33cec4"}
5120f313-21c3-4f4a-b888-9529e029e3ac	Fiscalis Mobile App	fa095a27-4e47-4099-b6a4-f4bd34650fbc	2026-06-04 17:32:06.081975-04	EXITOSO	{"modulo": "infraccion_vehicular", "acta_id": "80fa86ea-ea46-4cf8-a02a-07245c44e860"}
fde18195-fa5d-4bbe-bc62-c2c2e9468c84	Fiscalis Mobile App	fa095a27-4e47-4099-b6a4-f4bd34650fbc	2026-06-04 17:33:50.331346-04	EXITOSO	{"modulo": "infraccion_vehicular", "acta_id": "aa8236e9-59cf-4cc2-b4b2-7d19d1e6ba55"}
f8aaab08-733f-4709-83ef-680e2872a206	Fiscalis Mobile App	fa095a27-4e47-4099-b6a4-f4bd34650fbc	2026-06-05 14:05:21.426225-04	EXITOSO	{"modulo": "infraccion_vehicular", "acta_id": "25a62aca-329d-42d8-a051-a034d41fb8db"}
ab009551-5773-46fb-8ce7-8b1c342f8ad8	Fiscalis Mobile App	fa095a27-4e47-4099-b6a4-f4bd34650fbc	2026-06-05 14:39:48.513951-04	EXITOSO	{"modulo": "infraccion_vehicular", "acta_id": "1038f711-b944-40d8-891e-5e77ce8b1a8e"}
4ecf4047-62a3-4950-95c7-6ac00ba20836	Fiscalis Mobile App	fa095a27-4e47-4099-b6a4-f4bd34650fbc	2026-06-05 14:41:58.360684-04	EXITOSO	{"modulo": "infraccion_vehicular", "acta_id": "b1373c24-da1a-4989-b7c2-c8504326d47e"}
5723af25-19b2-4717-a28c-2b36e12f3213	Fiscalis Mobile App	fa095a27-4e47-4099-b6a4-f4bd34650fbc	2026-06-05 14:41:58.404652-04	EXITOSO	{"modulo": "infraccion_vehicular", "acta_id": "2c4d888e-1198-4328-acb3-ae64d54c584d"}
5f45b19a-8db0-4114-8abf-5c3354d6d717	Fiscalis Mobile App	fa095a27-4e47-4099-b6a4-f4bd34650fbc	2026-06-05 14:41:58.486279-04	EXITOSO	{"modulo": "infraccion_vehicular", "acta_id": "8d5d3c56-65b5-4464-8787-630a21a54b72"}
1c2417f8-98f7-4e11-b2dd-e70ec6f52c31	Fiscalis Mobile App	fa095a27-4e47-4099-b6a4-f4bd34650fbc	2026-06-05 14:41:58.561725-04	EXITOSO	{"modulo": "infraccion_vehicular", "acta_id": "dafc59ee-e8a3-43a0-b79e-07a441c20b6b"}
\.


--
-- Data for Name: usuario_mfa; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.usuario_mfa (id, usuario_id, totp_secret_encrypted, enabled, confirmed_at, recovery_codes_encrypted) FROM stdin;
8befe6ea-1da7-4aa1-a4ad-b094e5f10a04	fa095a27-4e47-4099-b6a4-f4bd34650fbc	gAAAAABqIfL-VN2n7qV0qL51SXn-eY4VIsYv82uw95UUPjhyb8NBw5XsOGkaJxmf56FydJwWIYjSxqsMx9TG38xv6T0U1XKgzO9tH2SSIwufaDzrE7h8kr3F0bxqdXB6XEs2_Ayj2ez-	t	2026-06-04 21:50:18.032795	gAAAAABqIfL-qHWZtC7EIQreqNjbMbugSZzMskiVs8IMJsQB74s9x5huMynTKCz8WPtfx8vmdkxoLPPOx7F_XpHkWZZvJ0H6s6GElPptMSI-wkstY42vdyxhdUJ4LQo36G9g7e98RGzcRdWYBQNnQcOxdTSoqUwpWx2gdvYxQxPBYI225F5KxVQ=
\.


--
-- Name: catalogo_infracciones_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.catalogo_infracciones_id_seq', 1, false);


--
-- Name: roles_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.roles_id_seq', 1, true);


--
-- PostgreSQL database dump complete
--

\unrestrict DVsZ90eTEcqdCV3c2a8kL8rpbtynm2KQhFDSSi43Rw6ytMUNwauv0yytNKZSOxU

