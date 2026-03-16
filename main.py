import streamlit as st
# Importación de los módulos locales
import gastos
import musica
import actividades
import invitados

st.set_page_config(page_title="Gestor de Graduación", layout="wide")

st.title("🎓 Organización Fiesta de Graduación 2026")
st.markdown("---")

# Barra lateral para la navegación
st.sidebar.header("Menú de Control")
opcion = st.sidebar.radio("Ir a:", 
    ["Inicio", "Presupuesto", "Playlist", "Cronograma", "Invitados"])

# Lógica de enrutamiento
if opcion == "Inicio":
    st.subheader("¡Bienvenidos al Centro de Mando!")
    st.write("Selecciona una sección en el menú de la izquierda para empezar a trabajar.")
    st.image("https://images.unsplash.com/photo-1541339907198-e08756ebafe3?auto=format&fit=crop&w=500", caption="¡Ya casi somos libres!")

elif opcion == "Presupuesto":
    gastos.mostrar_gastos()

elif opcion == "Playlist":
    musica.mostrar_musica()

elif opcion == "Cronograma":
    actividades.mostrar_actividades()

elif opcion == "Invitados":
    invitados.mostrar_invitados()