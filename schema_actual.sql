--
-- PostgreSQL database dump
--

\restrict 3ErTnBmG20hCsPv6KVqtJhLqf6LVwPwMHl8j85ZVSNKHhpDstkn2ErobBhstXon

-- Dumped from database version 18.3
-- Dumped by pg_dump version 18.3

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
-- Name: postgis; Type: EXTENSION; Schema: -; Owner: -
--

CREATE EXTENSION IF NOT EXISTS postgis WITH SCHEMA public;


--
-- Name: EXTENSION postgis; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION postgis IS 'PostGIS geometry and geography spatial types and functions';


--
-- Name: uuid-ossp; Type: EXTENSION; Schema: -; Owner: -
--

CREATE EXTENSION IF NOT EXISTS "uuid-ossp" WITH SCHEMA public;


--
-- Name: EXTENSION "uuid-ossp"; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION "uuid-ossp" IS 'generate universally unique identifiers (UUIDs)';


--
-- Name: accion_auditoria_enum; Type: TYPE; Schema: public; Owner: postgres
--

CREATE TYPE public.accion_auditoria_enum AS ENUM (
    'INSERT',
    'UPDATE',
    'DELETE',
    'ANULAR'
);


ALTER TYPE public.accion_auditoria_enum OWNER TO postgres;

--
-- Name: modulo_enum; Type: TYPE; Schema: public; Owner: postgres
--

CREATE TYPE public.modulo_enum AS ENUM (
    'vehiculo',
    'comercio',
    'actividad',
    'documentacion'
);


ALTER TYPE public.modulo_enum OWNER TO postgres;

--
-- Name: tipo_acta_enum; Type: TYPE; Schema: public; Owner: postgres
--

CREATE TYPE public.tipo_acta_enum AS ENUM (
    'advertencia',
    'citacion',
    'multa'
);


ALTER TYPE public.tipo_acta_enum OWNER TO postgres;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: auditoria_eventos; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.auditoria_eventos (
    id uuid NOT NULL,
    entidad_id character varying NOT NULL,
    entidad_tipo character varying NOT NULL,
    accion character varying NOT NULL,
    usuario_id uuid,
    payload jsonb NOT NULL,
    fecha timestamp with time zone NOT NULL
);


ALTER TABLE public.auditoria_eventos OWNER TO postgres;

--
-- Name: catalogo_infracciones; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.catalogo_infracciones (
    id integer NOT NULL,
    codigo_ley character varying(50) NOT NULL,
    descripcion text NOT NULL,
    gravedad character varying(50) NOT NULL,
    costo_utm numeric(5,2)
);


ALTER TABLE public.catalogo_infracciones OWNER TO postgres;

--
-- Name: catalogo_infracciones_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.catalogo_infracciones_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.catalogo_infracciones_id_seq OWNER TO postgres;

--
-- Name: catalogo_infracciones_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.catalogo_infracciones_id_seq OWNED BY public.catalogo_infracciones.id;


--
-- Name: dispositivos_moviles; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.dispositivos_moviles (
    id uuid NOT NULL,
    usuario_id uuid,
    device_id character varying,
    nombre_dispositivo character varying,
    activo boolean DEFAULT true,
    revocado boolean DEFAULT false,
    last_seen_at character varying,
    estado character varying(20) DEFAULT 'ACTIVO'::character varying
);


ALTER TABLE public.dispositivos_moviles OWNER TO postgres;

--
-- Name: evidencias_fotograficas; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.evidencias_fotograficas (
    id uuid NOT NULL,
    registro_uuid uuid NOT NULL,
    hash_sha256 character varying NOT NULL
);


ALTER TABLE public.evidencias_fotograficas OWNER TO postgres;

--
-- Name: infracciones_vehiculares; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.infracciones_vehiculares (
    registro_uuid uuid NOT NULL,
    ppu character varying NOT NULL,
    marca character varying,
    tipo_vehiculo character varying,
    color character varying,
    tipo_infraccion_id integer,
    observaciones text NOT NULL,
    rut_infractor character varying,
    nombre_completo character varying
);


ALTER TABLE public.infracciones_vehiculares OWNER TO postgres;

--
-- Name: registros_base; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.registros_base (
    id uuid NOT NULL,
    inspector_id uuid NOT NULL,
    modulo character varying NOT NULL,
    estado character varying NOT NULL,
    fecha_emision timestamp with time zone NOT NULL,
    ubicacion public.geometry(Point,4326) NOT NULL,
    auditoria_jsonb jsonb
);


ALTER TABLE public.registros_base OWNER TO postgres;

--
-- Name: roles; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.roles (
    id integer NOT NULL,
    nombre character varying NOT NULL
);


ALTER TABLE public.roles OWNER TO postgres;

--
-- Name: roles_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.roles_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.roles_id_seq OWNER TO postgres;

--
-- Name: roles_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.roles_id_seq OWNED BY public.roles.id;


--
-- Name: sesiones_moviles; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.sesiones_moviles (
    id uuid DEFAULT public.uuid_generate_v4() NOT NULL,
    usuario_id uuid NOT NULL,
    dispositivo_id uuid NOT NULL,
    token_hash character varying(255) NOT NULL,
    creada_at timestamp with time zone DEFAULT CURRENT_TIMESTAMP,
    expira_at timestamp with time zone NOT NULL,
    revocada boolean DEFAULT false
);


ALTER TABLE public.sesiones_moviles OWNER TO postgres;

--
-- Name: sync_events; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.sync_events (
    id uuid NOT NULL,
    dispositivo_id character varying NOT NULL,
    inspector_id uuid NOT NULL,
    fecha_sync timestamp with time zone NOT NULL,
    estado character varying NOT NULL,
    detalles jsonb
);


ALTER TABLE public.sync_events OWNER TO postgres;

--
-- Name: usuario_mfa; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.usuario_mfa (
    id uuid NOT NULL,
    usuario_id uuid,
    totp_secret_encrypted character varying NOT NULL,
    enabled boolean DEFAULT false,
    confirmed_at character varying,
    recovery_codes_encrypted character varying
);


ALTER TABLE public.usuario_mfa OWNER TO postgres;

--
-- Name: usuarios; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.usuarios (
    id uuid NOT NULL,
    username character varying NOT NULL,
    hashed_password character varying NOT NULL,
    activo boolean NOT NULL,
    rol_id integer NOT NULL
);


ALTER TABLE public.usuarios OWNER TO postgres;

--
-- Name: catalogo_infracciones id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.catalogo_infracciones ALTER COLUMN id SET DEFAULT nextval('public.catalogo_infracciones_id_seq'::regclass);


--
-- Name: roles id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.roles ALTER COLUMN id SET DEFAULT nextval('public.roles_id_seq'::regclass);


--
-- Name: catalogo_infracciones catalogo_infracciones_codigo_ley_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.catalogo_infracciones
    ADD CONSTRAINT catalogo_infracciones_codigo_ley_key UNIQUE (codigo_ley);


--
-- Name: catalogo_infracciones catalogo_infracciones_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.catalogo_infracciones
    ADD CONSTRAINT catalogo_infracciones_pkey PRIMARY KEY (id);


--
-- Name: dispositivos_moviles dispositivos_moviles_device_id_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.dispositivos_moviles
    ADD CONSTRAINT dispositivos_moviles_device_id_key UNIQUE (device_id);


--
-- Name: dispositivos_moviles dispositivos_moviles_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.dispositivos_moviles
    ADD CONSTRAINT dispositivos_moviles_pkey PRIMARY KEY (id);


--
-- Name: auditoria_eventos pk_auditoria_eventos; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auditoria_eventos
    ADD CONSTRAINT pk_auditoria_eventos PRIMARY KEY (id);


--
-- Name: evidencias_fotograficas pk_evidencias_fotograficas; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.evidencias_fotograficas
    ADD CONSTRAINT pk_evidencias_fotograficas PRIMARY KEY (id);


--
-- Name: infracciones_vehiculares pk_infracciones_vehiculares; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.infracciones_vehiculares
    ADD CONSTRAINT pk_infracciones_vehiculares PRIMARY KEY (registro_uuid);


--
-- Name: registros_base pk_registros_base; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.registros_base
    ADD CONSTRAINT pk_registros_base PRIMARY KEY (id);


--
-- Name: roles pk_roles; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.roles
    ADD CONSTRAINT pk_roles PRIMARY KEY (id);


--
-- Name: sync_events pk_sync_events; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.sync_events
    ADD CONSTRAINT pk_sync_events PRIMARY KEY (id);


--
-- Name: usuarios pk_usuarios; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.usuarios
    ADD CONSTRAINT pk_usuarios PRIMARY KEY (id);


--
-- Name: sesiones_moviles sesiones_moviles_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.sesiones_moviles
    ADD CONSTRAINT sesiones_moviles_pkey PRIMARY KEY (id);


--
-- Name: sesiones_moviles sesiones_moviles_token_hash_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.sesiones_moviles
    ADD CONSTRAINT sesiones_moviles_token_hash_key UNIQUE (token_hash);


--
-- Name: evidencias_fotograficas uq_evidencia_registro_hash; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.evidencias_fotograficas
    ADD CONSTRAINT uq_evidencia_registro_hash UNIQUE (registro_uuid, hash_sha256);


--
-- Name: usuario_mfa usuario_mfa_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.usuario_mfa
    ADD CONSTRAINT usuario_mfa_pkey PRIMARY KEY (id);


--
-- Name: usuario_mfa usuario_mfa_usuario_id_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.usuario_mfa
    ADD CONSTRAINT usuario_mfa_usuario_id_key UNIQUE (usuario_id);


--
-- Name: idx_registros_base_auditoria; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX idx_registros_base_auditoria ON public.registros_base USING gin (auditoria_jsonb);


--
-- Name: idx_registros_base_ubicacion; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX idx_registros_base_ubicacion ON public.registros_base USING gist (ubicacion);


--
-- Name: ix_auditoria_eventos_entidad_id; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX ix_auditoria_eventos_entidad_id ON public.auditoria_eventos USING btree (entidad_id);


--
-- Name: ix_auditoria_eventos_entidad_tipo; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX ix_auditoria_eventos_entidad_tipo ON public.auditoria_eventos USING btree (entidad_tipo);


--
-- Name: ix_evidencias_fotograficas_registro_uuid; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX ix_evidencias_fotograficas_registro_uuid ON public.evidencias_fotograficas USING btree (registro_uuid);


--
-- Name: ix_infracciones_vehiculares_ppu; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX ix_infracciones_vehiculares_ppu ON public.infracciones_vehiculares USING btree (ppu);


--
-- Name: ix_infracciones_vehiculares_tipo_infraccion_id; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX ix_infracciones_vehiculares_tipo_infraccion_id ON public.infracciones_vehiculares USING btree (tipo_infraccion_id);


--
-- Name: ix_registros_base_estado; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX ix_registros_base_estado ON public.registros_base USING btree (estado);


--
-- Name: ix_registros_base_inspector_id; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX ix_registros_base_inspector_id ON public.registros_base USING btree (inspector_id);


--
-- Name: ix_registros_base_modulo; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX ix_registros_base_modulo ON public.registros_base USING btree (modulo);


--
-- Name: ix_roles_nombre; Type: INDEX; Schema: public; Owner: postgres
--

CREATE UNIQUE INDEX ix_roles_nombre ON public.roles USING btree (nombre);


--
-- Name: ix_sync_events_dispositivo_id; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX ix_sync_events_dispositivo_id ON public.sync_events USING btree (dispositivo_id);


--
-- Name: ix_usuarios_username; Type: INDEX; Schema: public; Owner: postgres
--

CREATE UNIQUE INDEX ix_usuarios_username ON public.usuarios USING btree (username);


--
-- Name: dispositivos_moviles dispositivos_moviles_usuario_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.dispositivos_moviles
    ADD CONSTRAINT dispositivos_moviles_usuario_id_fkey FOREIGN KEY (usuario_id) REFERENCES public.usuarios(id);


--
-- Name: auditoria_eventos fk_auditoria_eventos_usuario_id_usuarios; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auditoria_eventos
    ADD CONSTRAINT fk_auditoria_eventos_usuario_id_usuarios FOREIGN KEY (usuario_id) REFERENCES public.usuarios(id);


--
-- Name: evidencias_fotograficas fk_evidencias_fotograficas_registro_uuid_registros_base; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.evidencias_fotograficas
    ADD CONSTRAINT fk_evidencias_fotograficas_registro_uuid_registros_base FOREIGN KEY (registro_uuid) REFERENCES public.registros_base(id);


--
-- Name: infracciones_vehiculares fk_infraccion_catalogo; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.infracciones_vehiculares
    ADD CONSTRAINT fk_infraccion_catalogo FOREIGN KEY (tipo_infraccion_id) REFERENCES public.catalogo_infracciones(id);


--
-- Name: infracciones_vehiculares fk_infracciones_vehiculares_registro_uuid_registros_base; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.infracciones_vehiculares
    ADD CONSTRAINT fk_infracciones_vehiculares_registro_uuid_registros_base FOREIGN KEY (registro_uuid) REFERENCES public.registros_base(id);


--
-- Name: registros_base fk_registros_base_inspector_id_usuarios; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.registros_base
    ADD CONSTRAINT fk_registros_base_inspector_id_usuarios FOREIGN KEY (inspector_id) REFERENCES public.usuarios(id);


--
-- Name: sync_events fk_sync_events_inspector_id_usuarios; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.sync_events
    ADD CONSTRAINT fk_sync_events_inspector_id_usuarios FOREIGN KEY (inspector_id) REFERENCES public.usuarios(id);


--
-- Name: usuarios fk_usuarios_rol_id_roles; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.usuarios
    ADD CONSTRAINT fk_usuarios_rol_id_roles FOREIGN KEY (rol_id) REFERENCES public.roles(id);


--
-- Name: usuario_mfa usuario_mfa_usuario_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.usuario_mfa
    ADD CONSTRAINT usuario_mfa_usuario_id_fkey FOREIGN KEY (usuario_id) REFERENCES public.usuarios(id);


--
-- PostgreSQL database dump complete
--

\unrestrict 3ErTnBmG20hCsPv6KVqtJhLqf6LVwPwMHl8j85ZVSNKHhpDstkn2ErobBhstXon

